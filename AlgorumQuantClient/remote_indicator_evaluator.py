from datetime import datetime

import jsonpickle

from .algorum_types import *


class RemoteIndicatorEvaluator(object):
    def __init__(self, client,
                 symbol: TradeSymbol,
                 uid: str):
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

    def cci(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'CCI',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def close(self):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest('CLOSE', None)
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def cos(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'COS',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def dema(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'DEMA',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def doji(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'DOJI',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def dragonfly_doji(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'DRAGONFLYDOJI',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

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

    def engulfing_bear(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'ENGULFINGBEAR',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def engulfing_bull(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'ENGULFINGBULL',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def evening_doji_star(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'EVENINGDOJISTART',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def evening_star(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'EVENINGSTAR',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def four_price_doji(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'FOURPRICEDOJI',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def grave_stone_doji(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'GRAVESTONEDOJI',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def hammer(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'HAMMER',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def hanging_man(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'HANGINGMAN',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def high(self):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest('HIGH', None)
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def hma(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'HMA',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def inverted_hammer(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'INVERTEDHAMMER',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def kama(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'KAMA',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def long_legged_doji(self, period: float):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest(
                            'LONGLEGGEDDOJI',
                            {'period': period}
                        )
                    ]
                ), False), None))
        result_val = jsonpickle.decode(response.JsonData)
        return result_val[0]["Result"]

    def low(self):
        response = self.Client.execute_async(AlgorumWebsocketMessage(
            'get_indicators',
            AlgorumMessageType.Request,
            self.Client.CorIdCounter.increment(),
            jsonpickle.encode(
                GetIndicatorsRequest(
                    self.Uid,
                    [
                        IndicatorRequest('LOW', None)
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
