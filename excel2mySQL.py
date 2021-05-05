# -*- coding: utf-8 -*-
"""
Created by Leon at 4/28/2021

"""
__author__ = "Leon"
__version__ = "0.0.1"
__email__ = "yang.li@zillnk.com"

import pandas as pd
import os
import time
from getpass import getpass
from mysql.connector import connect, Error

cnt = 0

TestRecordInfo = {'Sn': '', 'RunMode': 'Auto', 'StartTime': '', 'StopTime': '', 'Station': 'PA00001', 'Status': '',
                  'UserName': 'Zillnk01', 'ProductNumber': 'RHS1160061', 'TestType': 'Prod', 'Rstate': 'R1D',
                  'TpName': 'RuVue', 'TpVer': '20210501', 'MpgName': '', 'MpgTestTime': '', 'AppRev': '',
                  'MpgDescription': '', 'MpName': '', 'MpStatus': '', 'MpTestTime': '', 'MpDataType': 'float',
                  'MpDescription': '', 'LimitDown': '', 'LimitUp': '', 'Unit': '', 'Result': ''}


def TestRecordInfoGen(Sn: str, RunMode: str, StartTime: str, StopTime: str, Status: str, MpgName: str, MpgTestTime: str,
                      MpgDescription: str, MpName: str, MpStatus: str, MpTestTime: str, MpDataType: str,
                      MpDescription: str,
                      LimitDown, LimitUp, Unit, Result, AppRev: str, Station: str = 'PA00001',
                      ProductNumber: str = 'RHS1160061', Rstate: str = 'R1D', TpVer: str = '20210501',
                      UserName: str = 'Zillnk01',
                      TestType: str = 'Prod'
                      ):
    TestRecordInfo = {'Sn': Sn, 'RunMode': RunMode, 'StartTime': StartTime, 'StopTime': StopTime, 'Station': Station,
                      'Status': Status,
                      'UserName': UserName, 'ProductNumber': ProductNumber, 'TestType': TestType, 'Rstate': Rstate,
                      'TpName': 'RuVue', 'TpVer': TpVer, 'MpgName': MpgName, 'MpgTestTime': MpgTestTime,
                      'AppRev': AppRev,
                      'MpgDescription': MpgDescription, 'MpName': MpName, 'MpStatus': MpStatus,
                      'MpTestTime': MpTestTime, 'MpDataType': MpDataType,
                      'MpDescription': MpDescription, 'LimitDown': LimitDown, 'LimitUp': LimitUp, 'Unit': Unit,
                      'Result': Result}

    return TestRecordInfo


def mysql_operate(TestRecordInfo: dict):
    global cnt
    cnt = cnt + 1
    print('cnt:', cnt, TestRecordInfo)
    update_query = """
        INSERT INTO
        `test_result_tbl`(
            `cnt`,
            `Sn`,
            `RunMode`,
            `StartTime`,
            `MpgName`,
            `MpgTestTime`,
            `AppRev`,
            `MpName`,
            `MpTestTime`,
            `LimitDown`,
            `LimitUp`,
            `Result`
        )
        VALUES(
                %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, %s
            );
        """ % (
        # Sn, RunMode, StartTime, MpgName, MpgTestTime, AppRev, MpName, MpTestTime, LimitDown, LimitUp, Result
        cnt, TestRecordInfo['Sn'], TestRecordInfo['RunMode'], TestRecordInfo['StartTime'],
        TestRecordInfo['MpgName'], TestRecordInfo['MpgTestTime'], TestRecordInfo['AppRev'], TestRecordInfo['MpName'],
        TestRecordInfo['MpTestTime'], TestRecordInfo['LimitDown'], TestRecordInfo['LimitUp'], TestRecordInfo['Result']

    )
    # print(update_query)
    # time.sleep(0.5)
    try:
        with connection.cursor() as cursor:
            for result in cursor.execute(update_query, multi=True):
                if result.with_rows:
                    print(result.fetchall())
            connection.commit()
            # time.sleep(1)
    except:
        print('sql operation failed!')
        return


def show(p, filter=None):
    cnt = 0
    for root, dirs, files in os.walk(p):
        for f in files:
            filename = str(f)
            if not filter:
                print(os.path.join(root, filename))
            elif os.path.splitext(filename)[-1] == filter:  # string you want to rename
                try:
                    # os.rename(os.path.join(root , f), os.path.join(root , renames[f]))
                    # print("Renaming ",f,"to",renames[f])
                    # print(os.path.join(root, filename))
                    path = os.path.join(root, filename)
                    info = read_info(path)
                    if not info:
                        # print(path)
                        continue
                    else:
                        ""
                        # print(cnt, ':', info)
                        # cnt = cnt + 1
                except FileNotFoundError as e:
                    print(str(e))


def read_sn(file):
    try:
        xls = pd.ExcelFile(file)
        if 'Prod Info' in xls.sheet_names:
            info = xls.parse('Prod Info', header=None)
            # return info.values[1, 1]
            d = {}
            for i in info.index:
                cell_name = info.values[i, 0]
                cell_value = info.values[i, 1]
                # d[cell_name] = cell_value
                if 'Serial Number' in cell_name:
                    return cell_value

            return None
        else:
            return None
    except:
        return None


# def read_info(file):
#     try:
#         xls = pd.ExcelFile(file)
#         if 'Prod Info' in xls.sheet_names:
#             info = xls.parse('Prod Info', header=None)
#             #return info.values[1, 1]
#             d = {}
#             for i in info.index:
#                 cell_name = info.values[i, 0]
#                 cell_value = info.values[i, 1]
#                 d[cell_name] = cell_value
#
#             if 'Serial Number' in d and 'SW info' in d and 'Test Date' in d and "ZSM_20210407_ST_Cpri_Clock_01" in d['SW info']:
#                 #print(d['Serial Number'], ': ', d['SW info'])
#                 return d['Serial Number'] + ":" + d['SW info'] + ":" + d['Test Date']
#
#         else:
#             return None
#     except:
#         return None


def read_rx_gain(file):
    try:
        xls = pd.ExcelFile(file)
        if 'Prod Info' in xls.sheet_names and 'rx_calib' in xls.sheet_names:
            # print(file)
            info = xls.parse('Prod Info', header=None)
            # return info.values[1, 1]
            d = {}
            for i in info.index:
                cell_name = info.values[i, 0]
                cell_value = info.values[i, 1]
                d[cell_name] = cell_value

            if 'Serial Number' in d and 'SW info' in d and 'Test Date' in d and "ZSM_20210407_ST_Cpri_Clock_01" in d[
                'SW info']:
                # print(d['Serial Number'], ': ', d['SW info'])
                info = d['Serial Number'] + ":" + d['SW info'] + ":" + d['Test Date']
            else:
                return None
            rx_calib = xls.parse('rx_calib', header=None)
            # print(rx_calib.values)
            gain_A = rx_calib.values[1, 2]
            gain_B = rx_calib.values[14, 2]
            gain_C = rx_calib.values[27, 2]
            gain_D = rx_calib.values[40, 2]
            # print(info, ': rx branch  A gain = ', gain)
            return info + ': rx branch  A gain = ' + str(gain_A) + ': rx branch  B gain = ' + str(
                gain_B) + ': rx branch  C gain = ' + str(gain_C) + ': rx branch  D gain = ' + str(gain_D)
        else:
            return None
    except:
        return None


def date_str_conv(date: str):
    date = date.split('-')
    return date[0] + '-' + date[1] + '-' + date[2] + ' ' + date[3] + ':' + date[4] + ':' + date[5]


def read_info(file):
    try:
        xls = pd.ExcelFile(file)
        if 'Prod Info' in xls.sheet_names:
            # print(file)
            info = xls.parse('Prod Info', header=None)
            # return info.values[1, 1]
            d = {}
            for i in info.index:
                cell_name = info.values[i, 0]
                cell_value = info.values[i, 1]
                d[cell_name] = cell_value

            if 'Serial Number' in d and 'SW info' in d and 'Test Date' in d and "ZSM_20210407_ST_Cpri_Clock_01" in d[
                'SW info']:
                # print(d['Serial Number'], ': ', d['SW info'])
                info = d['Serial Number'] + ":" + d['SW info'] + ":" + date_str_conv(d['Test Date'])

                ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                             StartTime=date_str_conv(d['Test Date']), StopTime="",
                                             Status="", MpgName="", MpgTestTime="", AppRev=d['SW info'],
                                             MpgDescription="", MpName="", MpStatus="", MpTestTime="", MpDataType="",
                                             MpDescription="",
                                             LimitDown="", LimitUp="", Unit="", Result="")
            else:
                return None

            for sheet in xls.sheet_names:

                if 'rx_calib' in xls.sheet_names:
                    rx_calib = xls.parse('rx_calib', header=None)
                    # print(rx_calib.values)
                    gain_A = rx_calib.values[1, 2] - rx_calib.values[1, 1]
                    gain_B = rx_calib.values[14, 2] - rx_calib.values[14, 1]
                    gain_C = rx_calib.values[27, 2] - rx_calib.values[27, 1]
                    gain_D = rx_calib.values[40, 2] - rx_calib.values[40, 1]
                    gain = [gain_A, gain_B, gain_C, gain_D]
                    temp = [rx_calib.values[1, 3], rx_calib.values[14, 3], rx_calib.values[27, 3],
                            rx_calib.values[40, 3]]
                    freq_comp_tbl = {
                        rx_calib.values[1, 0]: dict(zip(rx_calib.values[3:14, 1],
                                                        rx_calib.values[1, 2] - (rx_calib.values[3:14, 2] + 50))),
                        rx_calib.values[14, 0]: dict(zip(rx_calib.values[16:27, 1],
                                                         rx_calib.values[14, 2] - (rx_calib.values[16:27, 2] + 50))),
                        rx_calib.values[27, 0]: dict(zip(rx_calib.values[29:40, 1],
                                                         rx_calib.values[27, 2] - (rx_calib.values[29:40, 2] + 50))),
                        rx_calib.values[40, 0]: dict(zip(rx_calib.values[42:53, 1],
                                                         rx_calib.values[40, 2] - (rx_calib.values[42:53, 2] + 50))),
                    }

                    # print(info, ': rx branch  A gain = ', gain)
                    # return info + ': rx branch  A gain = ' + str(gain_A) + ': rx branch  B gain = ' + str(gain_B)+ ': rx branch  C gain = ' + str(gain_C)+ ': rx branch  D gain = ' + str(gain_D)
                    # print(info + 'gain= ' + str(gain) + 'temp = ' + str(temp) + 'freqComTab =: ' + str(freq_comp_tbl))
                    for index, branch in enumerate(['A', 'B', 'C', 'D']):
                        # ProdInfo['']
                        # print(index, ':', branch)

                        # UL calib gain
                        MpgName = 'Rx Calib Gain'
                        MpgTestTime = date_str_conv(d['Test Date'])
                        MpgDescription = 'Rx calibration'
                        MpName = f'rx gain 3700MHz Branch {branch}'
                        MpTestTime = date_str_conv(d['Test Date'])
                        MpDataType = 'DOUBLE'
                        MpDescription = f'Rx frontend gain at center frequency Branch {branch}'
                        LimitDown = 28
                        LimitUp = 35
                        Unit = 'dB'
                        Result = float(gain[index])
                        MpStatus = 'pass' if (Result > LimitDown and Result < LimitUp) else 'fail'

                        ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                                     StartTime=date_str_conv(d['Test Date']),
                                                     StopTime="",
                                                     Status="", MpgName=MpgName, MpgTestTime=MpgTestTime,
                                                     AppRev=d['SW info'],
                                                     MpgDescription=MpgDescription, MpName=MpName, MpStatus=MpStatus,
                                                     MpTestTime=MpTestTime,
                                                     MpDataType=MpDataType, MpDescription=MpDescription,
                                                     LimitDown=LimitDown, LimitUp=LimitUp, Unit=Unit, Result=Result)
                        # print(ProdInfo)
                        mysql_operate(ProdInfo)
                        # UL  temperature
                        MpgName = 'Rx Temperature'
                        MpgTestTime = date_str_conv(d['Test Date'])
                        MpgDescription = f'Rx Temperature during calibration'
                        MpName = f'rx temperature Branch {branch}'
                        MpTestTime = date_str_conv(d['Test Date'])
                        MpDataType = 'DOUBLE'
                        MpDescription = f'Rx Temperature during calibration Branch {branch}'
                        LimitDown = 10
                        LimitUp = 50
                        Unit = '°C'
                        Result = float(gain[index])
                        MpStatus = 'pass' if (Result > LimitDown and Result < LimitUp) else 'fail'

                        ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                                     StartTime=date_str_conv(d['Test Date']),
                                                     StopTime="",
                                                     Status="", MpgName=MpgName, MpgTestTime=MpgTestTime,
                                                     AppRev=d['SW info'],
                                                     MpgDescription=MpgDescription, MpName=MpName, MpStatus=MpStatus,
                                                     MpTestTime=MpTestTime,
                                                     MpDataType=MpDataType, MpDescription=MpDescription,
                                                     LimitDown=LimitDown, LimitUp=LimitUp, Unit=Unit, Result=Result)
                        # print(ProdInfo)
                        mysql_operate(ProdInfo)
                        for freq in freq_comp_tbl[branch].keys():
                            MpgName = 'Rx Calib Freq Comp'
                            MpgTestTime = date_str_conv(d['Test Date'])
                            MpgDescription = f'Rx Frequency Compensation Table'
                            MpName = f'rx FreqCompTab Branch {branch} @Freq= {freq} MHz'
                            MpTestTime = date_str_conv(d['Test Date'])
                            MpDataType = 'DOUBLE'
                            MpDescription = f'rx FreqCompTab Branch {branch} @Freq= {freq} MHz'
                            LimitDown = -10.0
                            LimitUp = 5.0
                            Unit = 'dB'
                            Result = freq_comp_tbl[branch][freq]
                            MpStatus = 'pass' if (Result > LimitDown and Result < LimitUp) else 'fail'

                            ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                                         StartTime=date_str_conv(d['Test Date']),
                                                         StopTime="",
                                                         Status="", MpgName=MpgName, MpgTestTime=MpgTestTime,
                                                         AppRev=d['SW info'],
                                                         MpgDescription=MpgDescription, MpName=MpName,
                                                         MpStatus=MpStatus,
                                                         MpTestTime=MpTestTime,
                                                         MpDataType=MpDataType, MpDescription=MpDescription,
                                                         LimitDown=LimitDown, LimitUp=LimitUp, Unit=Unit, Result=Result)
                            # print(ProdInfo)
                            mysql_operate(ProdInfo)

                if 'tx_calib' in xls.sheet_names:
                    print(cnt)
                    tx_calib = xls.parse('tx_calib', header=None)
                    # print(rx_calib.values)
                    tx_init_A = tx_calib.values[1, 1]
                    tx_init_B = tx_calib.values[2, 1]
                    tx_init_C = tx_calib.values[3, 1]
                    tx_init_D = tx_calib.values[4, 1]

                    tor_init_A = tx_calib.values[1, 3]
                    tor_init_B = tx_calib.values[2, 3]
                    tor_init_C = tx_calib.values[3, 3]
                    tor_init_D = tx_calib.values[4, 3]

                    tx_init = [tx_init_A, tx_init_B, tx_init_C, tx_init_D]
                    tor_init = [tor_init_A, tor_init_B, tor_init_C, tor_init_D]

                    tor_freq_comp_tbl = {
                        tx_calib.values[1, 0]: dict(zip(tx_calib.values[6:16, 1] + 3700,
                                                        0.5 + (-18 - tx_calib.values[6:16, 3]) - (43 - tx_calib.values[6:16, 2]))),
                        tx_calib.values[2, 0]: dict(zip(tx_calib.values[17:27, 1] + 3700,
                                                         0.5 + (-18 - tx_calib.values[17:27, 3]) - (43 - tx_calib.values[17:27, 2]))),
                        tx_calib.values[3, 0]: dict(zip(tx_calib.values[28:38, 1] + 3700,
                                                         0.5 + (-18 - tx_calib.values[28:38, 3]) - (43 - tx_calib.values[28:38, 2]))),
                        tx_calib.values[4, 0]: dict(zip(tx_calib.values[39:49, 1] + 3700,
                                                        0.5 + (-18 - tx_calib.values[39:49, 3]) - (
                                                                    43 - tx_calib.values[39:49, 2]))),
                    }

                    # print(info, ': rx branch  A gain = ', gain)
                    # return info + ': rx branch  A gain = ' + str(gain_A) + ': rx branch  B gain = ' + str(gain_B)+ ': rx branch  C gain = ' + str(gain_C)+ ': rx branch  D gain = ' + str(gain_D)
                    # print(info + 'gain= ' + str(gain) + 'temp = ' + str(temp) + 'freqComTab =: ' + str(freq_comp_tbl))
                    for index, branch in enumerate(['A', 'B', 'C', 'D']):
                        # ProdInfo['']
                        # print(index, ':', branch)

                        # tx init dsa
                        MpgName = 'Tx Calib'
                        MpgTestTime = date_str_conv(d['Test Date'])
                        MpgDescription = 'Tx calibration'
                        MpName = f'Tx Init DSA Branch {branch}'
                        MpTestTime = date_str_conv(d['Test Date'])
                        MpDataType = 'INT'
                        MpDescription = f'Tx INIT DSA value Branch {branch} for ARP=43dBm'
                        LimitDown = 11
                        LimitUp = 20
                        Unit = 'dB'
                        Result = tx_init[index]
                        MpStatus = 'pass' if (Result > LimitDown and Result < LimitUp) else 'fail'

                        ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                                     StartTime=date_str_conv(d['Test Date']),
                                                     StopTime="",
                                                     Status="", MpgName=MpgName, MpgTestTime=MpgTestTime,
                                                     AppRev=d['SW info'],
                                                     MpgDescription=MpgDescription, MpName=MpName, MpStatus=MpStatus,
                                                     MpTestTime=MpTestTime,
                                                     MpDataType=MpDataType, MpDescription=MpDescription,
                                                     LimitDown=LimitDown, LimitUp=LimitUp, Unit=Unit, Result=Result)
                        # print(ProdInfo)
                        mysql_operate(ProdInfo)
                        # Tor init
                        MpgName = 'Tx Calib'
                        MpgTestTime = date_str_conv(d['Test Date'])
                        MpgDescription = 'Tx calibration'
                        MpName = f'Tor Init DSA Branch {branch}'
                        MpTestTime = date_str_conv(d['Test Date'])
                        MpDataType = 'INT'
                        MpDescription = f'Tor INIT DSA value Branch {branch}'
                        LimitDown = 5
                        LimitUp = 9
                        Unit = 'dB'
                        Result = tor_init[index]
                        MpStatus = 'pass' if (Result > LimitDown and Result < LimitUp) else 'fail'

                        ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                                     StartTime=date_str_conv(d['Test Date']),
                                                     StopTime="",
                                                     Status="", MpgName=MpgName, MpgTestTime=MpgTestTime,
                                                     AppRev=d['SW info'],
                                                     MpgDescription=MpgDescription, MpName=MpName, MpStatus=MpStatus,
                                                     MpTestTime=MpTestTime,
                                                     MpDataType=MpDataType, MpDescription=MpDescription,
                                                     LimitDown=LimitDown, LimitUp=LimitUp, Unit=Unit, Result=Result)
                        # print(ProdInfo)
                        mysql_operate(ProdInfo)
                        for freq in tor_freq_comp_tbl[branch].keys():
                            MpgName = 'Tor Calib '
                            MpgTestTime = date_str_conv(d['Test Date'])
                            MpgDescription = f'Tx Calibration'
                            MpName = f'Tor FreqCompTab Branch {branch} @Freq= {freq} MHz'
                            MpTestTime = date_str_conv(d['Test Date'])
                            MpDataType = 'DOUBLE'
                            MpDescription = f'Tor FreqCompTab Branch {branch} @Freq= {freq} MHz'
                            LimitDown = -1.5
                            LimitUp = 1.5
                            Unit = 'dB'
                            Result = tor_freq_comp_tbl[branch][freq]
                            MpStatus = 'pass' if (Result > LimitDown and Result < LimitUp) else 'fail'

                            ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                                         StartTime=date_str_conv(d['Test Date']),
                                                         StopTime="",
                                                         Status="", MpgName=MpgName, MpgTestTime=MpgTestTime,
                                                         AppRev=d['SW info'],
                                                         MpgDescription=MpgDescription, MpName=MpName,
                                                         MpStatus=MpStatus,
                                                         MpTestTime=MpTestTime,
                                                         MpDataType=MpDataType, MpDescription=MpDescription,
                                                         LimitDown=LimitDown, LimitUp=LimitUp, Unit=Unit, Result=Result)
                            # print(ProdInfo)
                            mysql_operate(ProdInfo)

                if 'pa bias calib' in xls.sheet_names:
                    pa_calib = xls.parse('pa bias calib', header=None)
                    # print(rx_calib.values)

                    temp = [pa_calib.values[1, 9], pa_calib.values[2, 9], pa_calib.values[3, 9],
                            pa_calib.values[4, 9]]

                    for index, branch in enumerate(['A', 'B', 'C', 'D']):
                        MpgName = 'PA Calib  '
                        MpgTestTime = date_str_conv(d['Test Date'])
                        MpgDescription = f'PA Calib'
                        MpName = f'PA Branch {branch} Temperature'
                        MpTestTime = date_str_conv(d['Test Date'])
                        MpDataType = 'DOUBLE'
                        MpDescription = f'PA Branch {branch} Temperature During bias calibration'
                        LimitDown = 10.0
                        LimitUp = 50.0
                        Unit = '°C'
                        Result = temp[index]
                        MpStatus = 'pass' if (Result > LimitDown and Result < LimitUp) else 'fail'

                        ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                                     StartTime=date_str_conv(d['Test Date']),
                                                     StopTime="",
                                                     Status="", MpgName=MpgName, MpgTestTime=MpgTestTime,
                                                     AppRev=d['SW info'],
                                                     MpgDescription=MpgDescription, MpName=MpName,
                                                     MpStatus=MpStatus,
                                                     MpTestTime=MpTestTime,
                                                     MpDataType=MpDataType, MpDescription=MpDescription,
                                                     LimitDown=LimitDown, LimitUp=LimitUp, Unit=Unit, Result=Result)
                        # print(ProdInfo)
                        mysql_operate(ProdInfo)

                        for sub_index, pos in enumerate(['Final Main', 'Final Peak', 'Driver Main', 'Driver Peak']):
                            MpgName = 'PA Bias Calib'
                            MpgTestTime = date_str_conv(d['Test Date'])
                            MpgDescription = f'PA Bias Calib'
                            MpName = f'PA Branch {branch} {pos}Bias Calib'
                            MpTestTime = date_str_conv(d['Test Date'])
                            MpDataType = 'DOUBLE'
                            MpDescription = f'PA Branch {branch} {pos} bias calibration'
                            LimitDown = 400
                            LimitUp = 2500
                            Unit = '°C'
                            Result = pa_calib.values[index + 1, sub_index + 2]
                            MpStatus = 'pass' if (Result > LimitDown and Result < LimitUp) else 'fail'

                            ProdInfo = TestRecordInfoGen(Sn=d['Serial Number'], RunMode='Prod',
                                                         StartTime=date_str_conv(d['Test Date']),
                                                         StopTime="",
                                                         Status="", MpgName=MpgName, MpgTestTime=MpgTestTime,
                                                         AppRev=d['SW info'],
                                                         MpgDescription=MpgDescription, MpName=MpName,
                                                         MpStatus=MpStatus,
                                                         MpTestTime=MpTestTime,
                                                         MpDataType=MpDataType, MpDescription=MpDescription,
                                                         LimitDown=LimitDown, LimitUp=LimitUp, Unit=Unit,
                                                         Result=Result)
                            mysql_operate(ProdInfo)




            # return info + ' gain= ' + str(gain) + 'temp = ' + str(temp) + 'freqComTab =: ' + str(freq_comp_tbl)
            return (ProdInfo)
        else:
            return None

    except:
        return None

try:
    connection = connect(
        host="localhost",
        user="root",
        password="oppaha89",
        database="oru1226n78a",
    )
except Error as e:
    print(e)

path = r"\\172.16.1.11\\产品开发-公用\\test\\ORU1226 N77A\\2021"
show(p=path, filter='.xlsx')

file = r'\\172.16.1.11\产品开发-公用\test\ORU1226 N77A\2021\Z122601202102000014\20210416174240_TX & RX Cal\160_Z122601202102000014_result_20210416174519.xlsx'
# print(read_info(file))
# xls = pd.ExcelFile(file)

# for sheet in xls.sheet_names:
#     print(sheet)

# if 'Prod Info' in xls.sheet_names:
#     info = xls.parse('Prod Info', header=None)
#     print(info.values[1, 1])
#     #print(type(info))
