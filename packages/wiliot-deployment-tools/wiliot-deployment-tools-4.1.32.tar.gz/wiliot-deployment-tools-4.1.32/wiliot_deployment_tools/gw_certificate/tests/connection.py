import datetime
import time
from wiliot_deployment_tools.common.debug import debug_print
from wiliot_deployment_tools.gw_certificate.api_if.gw_capabilities import GWCapabilities
from wiliot_deployment_tools.gw_certificate.tests.generic import PassCriteria, MINIMUM_SCORE, PERFECT_SCORE, GenericStage, GenericTest
from wiliot_deployment_tools.gw_certificate.api_if.api_validation import validate_message, MESSAGE_TYPES
from wiliot_deployment_tools.interface.mqtt import MqttClient
from wiliot_deployment_tools.interface.ble_sniffer import BLESniffer, BLESnifferContext
import pkg_resources
import pandas as pd
import ast
from packaging import version


CHANNELS_TO_ANALYZE = [37, 38, 39]
LISTEN_TIME_SEC = 30
MAX_UNSIGNED_32_BIT = 4294967295
CSV_NAME = 'bad_crc_to_PER_quantization.csv'
REQ_FW_VER = "4.2.0"

class ConnectionStage(GenericStage):
    def __init__(self, sniffer:BLESniffer , mqttc:MqttClient, **kwargs):
        self.mqttc = mqttc
        self.sniffer = sniffer
        self.conversion_table_df = None
        self.__dict__.update(kwargs)
        super().__init__(stage_name=type(self).__name__, **self.__dict__)

    def is_version_greater(self, checked_version, req_version):
        # The checked_version is already parsed 
        v1 = checked_version
        v2 = version.parse(req_version)
        return v1 >= v2

    def get_data_from_quantization_csv(self):
        relative_path = CSV_NAME
        csv_path = pkg_resources.resource_filename(__name__, relative_path)
        conversion_table_df = pd.read_csv(csv_path)
        self.conversion_table_df = conversion_table_df

    def interference_analysis(self):
        """Analyze the interference level (PER) before the test begins

        """ 
        def handle_wrap_around(a, b, c):
            # To handle a wrap arround of the counter
            if a < 0:
                a = a + MAX_UNSIGNED_32_BIT
            if b < 0:
                b = b + MAX_UNSIGNED_32_BIT
            if c < 0:
                c = c + MAX_UNSIGNED_32_BIT

        for channel in CHANNELS_TO_ANALYZE:
            # Send the sniffer a command to retrive the counters and convert them to dict
            self.sniffer.start_cntr_extractor_sniffer(rx_channel=channel)
            cntrs_string_start = self.sniffer.get_pkts_cntrs()
            cntrs_dict_start = ast.literal_eval(cntrs_string_start)
            debug_print(f'Analyzing channel {channel}...')
            time.sleep(LISTEN_TIME_SEC)
            cntrs_string_end = self.sniffer.get_pkts_cntrs()
            cntrs_dict_end = ast.literal_eval(cntrs_string_end)
            self.sniffer.stop_sniffer()

            if cntrs_dict_start == None or cntrs_dict_end == None:
                debug_print(f'Channel {channel} interference analysis was skipped beacaus at least one counter is missing.')
                self.add_to_stage_report(f'Channel {channel} Ambient Interference was not calculated, missing at least one counter.')
                continue

            # Calculate the bad CRC percentage
            wlt_pkts =  cntrs_dict_end['wlt_rx'] - cntrs_dict_start['wlt_rx']
            non_wlt_pkts = cntrs_dict_end['non_wlt_rx'] - cntrs_dict_start['non_wlt_rx']
            bad_crc_pkts = cntrs_dict_end['bad_crc'] - cntrs_dict_start['bad_crc']
            handle_wrap_around(wlt_pkts, non_wlt_pkts, bad_crc_pkts)
            bad_crc_percentage = round((bad_crc_pkts / (wlt_pkts + non_wlt_pkts)) * 100)
            self.add_to_stage_report(f'Channel {channel} Ambient Interference (bad CRC percentage) is: {bad_crc_percentage}%. Good CRC packets = {wlt_pkts + non_wlt_pkts - bad_crc_pkts}, bad CRC packets: {bad_crc_pkts}')

            # Uncomment if you want to see PER of the site (will require print adjustments). Below, we use the truth table from the csv to match PER the bad CRC percentage. Require an update of the CSV to the bridge-GW case
            # closest_index = (self.conversion_table_df['bad_crc_percent'] - bad_crc_percentage).abs().idxmin()
            # per_percent = self.conversion_table_df.iloc[closest_index]['per_percent']
            # self.add_to_stage_report(f'Channel {channel} PER is: {per_percent}%')

    def run(self):
        self.stage_pass = MINIMUM_SCORE
        input('Please unplug GW from power. Press enter when unplugged')
        self.mqttc.flush_messages()
        input('Please plug GW back to power. Press enter when plugged')
        debug_print('Waiting for GW to connect... (Timeout 3 minutes)')
        timeout = datetime.datetime.now() + datetime.timedelta(minutes=3)
        status_message = None
        while datetime.datetime.now() < timeout and status_message is None:
            status_message = self.mqttc.get_status_message()
        if status_message is not None:
            self.add_to_stage_report('GW Status packet received:')
            debug_print(status_message)
            validation = validate_message(MESSAGE_TYPES.STATUS, status_message, data_type=None)
            self.stage_pass = PERFECT_SCORE if validation[0] else MINIMUM_SCORE
            # set GW Capabilities:
            for key, value in status_message.items():
                if key in GWCapabilities.get_capabilities() and type(value) is bool:
                    self.gw_capabilities.set_capability(key, value)
                    self.add_to_stage_report(f'Set Capability: {key} - {value}')
            # Add reason test failed to report if neccessary
            self.add_to_stage_report(validation[1]) if self.stage_pass == MINIMUM_SCORE else None
            # Add status packet to test report
            self.add_to_stage_report(str(status_message))
        else:
            self.add_to_stage_report("No message recieved from GW in status topic after 3 mins")
        
        # Run interference analysis
        # Note: there is an infrastructure for converting bad_CRC % to PER, currently unused and commented since the quantization_csv does not match the bridge to GW case.
        sniffer_board_version = self.sniffer.uart.fw_version
        self.add_to_stage_report("-----------------------------")
        if self.is_version_greater(sniffer_board_version, REQ_FW_VER):
            debug_print(f"Start interference analysis for channels {CHANNELS_TO_ANALYZE}. This will take {30 * len(CHANNELS_TO_ANALYZE)} secondes")
            # self.get_data_from_quantization_csv()
            self.add_to_stage_report("Interference Analysis Report:")
            self.interference_analysis()
        else:
            debug_print(f"Interference analysis is available only from FW version 4.2.x, but the board's version is {sniffer_board_version}")
            self.add_to_stage_report(f"Interference analysis skipped due to inferior board version ({sniffer_board_version})")
    
    def generate_stage_report(self):
        self.report_html = self.template_engine.render_template('stage.html', stage_name = self.stage_name, stage_pass=self.stage_pass, 
                                                                pass_min=self.pass_min, inconclusive_min=self.inconclusive_min, stage_report=self.report.split('\n'))
        debug_print(self.report)
        return super().generate_stage_report()
    

class ConnectionTest(GenericTest):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__(**self.__dict__, test_name=type(self).__name__)
        self.stages = [ConnectionStage(**self.__dict__)]
        
    def run(self):
        super().run()
        self.test_pass = PERFECT_SCORE
        for stage in self.stages:
            stage.prepare_stage()
            stage.run()
            if (stage.stage_pass < self.test_pass):
                self.test_pass = stage.stage_pass
            self.add_to_test_report(stage.generate_stage_report())
