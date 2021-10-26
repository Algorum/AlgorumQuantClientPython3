from datetime import datetime

import jsonpickle

from .algorum_types import *


class RemoteIndicatorEvaluator(object):
    def __init__(self, client,
                 symbol: TradeSymbol,
                 uid: str) -> object:
        self.Uid = uid
        self.Symbol = symbol
        self.Client = client

    def ema(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'EMA',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def abandoned_baby_bear(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'ABANDONEDBABYBEAR',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def abandoned_baby_bull(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'ABANDONEDBABYBULL',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def ad(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'AD',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def adosc(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'ADOSC',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def adx(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'ADX',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def adxr(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'ADXR',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def ao(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'AO',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def apo(self, short_period: float, long_period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'APO',
                            {
                                'shortPeriod': short_period,
                                'longPeriod': long_period
                            }
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def aroon_down(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'AROONDOWN',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def aroon_osc(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'AROONOSC',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def aroon_up(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'AROONUP',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def atr(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'ATR',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def avg_price(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'AVGPRICE',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def bband_lower(self, period: float, stddev: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'BBANDLOWER',
                            {
                                'period': period,
                                'stddev': stddev
                            }
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def bband_mid(self, period: float, stddev: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'BBANDMID',
                            {
                                'period': period,
                                'stddev': stddev
                            }
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def bband_up(self, period: float, stddev: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'BBANDUP',
                            {
                                'period': period,
                                'stddev': stddev
                            }
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def big_black_candle(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'BIGBLACKCANDLE',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def black_marubozu(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'BLACKMARUBOZU',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def bop(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'BOP',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def candle_close(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'CANDLECLOSE',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def candle_high(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'CANDLEHIGH',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def candle_low(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'CANDLELOW',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def candle_open(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'CANDLEOPEN',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def preload_candles(self, candle_count: int, preload_end_time: datetime, api_key: str,
                        api_secret_key: str):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'preload_candles',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                PreloadCandlesRequest(self.Uid, candle_count, preload_end_time, api_key, api_secret_key),
                False), None))
