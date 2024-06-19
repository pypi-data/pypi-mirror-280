import os
from enum import Enum

from finter.data import ModelData
from finter.performance import Evaluator, get_bench_cm


class ModelTypeConfig(Enum):
    ALPHA = {"class_name": "Alpha", "file_name": "am.py"}
    PORTFOLIO = {"class_name": "Portfolio", "file_name": "pf.py"}
    FLEXIBLE_FUND = {"class_name": "FlexibleFund", "file_name": "ffd.py"}

    @property
    def class_name(self):
        return self.value["class_name"]

    @property
    def file_name(self):
        return self.value["file_name"]

    @classmethod
    def available_options(cls):
        return ", ".join([item.name for item in cls])


class Benchmark(Enum):
    CSI300 = "CSI300"
    DAX = "DAX"
    DJIA = "DJIA"
    HANGSENG = "HANGSENG"
    KOSDAQ = "KOSDAQ"
    KOSPI = "KOSPI"
    KOSPI200 = "KOSPI200"
    KOSPI_LARGECAP = "KOSPI_LARGECAP"
    KOSPI_MIDCAP = "KOSPI_MIDCAP"
    KOSPI_SMALLCAP = "KOSPI_SMALLCAP"
    MSCI_US_REIT = "MSCI_US_REIT"
    NASDAQ100 = "NASDAQ100"
    NASDAQ_COMPOSITE = "NASDAQ_COMPOSITE"
    SP500 = "S&P500"
    SP_GSCI = "S&P_GSCI"
    SP_GSCI_CRUDE = "S&P_GSCI_CRUDE"
    SP_GSCI_PM = "S&P_GSCI_PM"
    STOXX50 = "STOXX50"
    STOXX600 = "STOXX600"
    US_DOLLAR = "US_DOLLAR"
    VIX = "VIX"
    CANADA_SP_TSX = "CANADA_S_P_TSX"
    DOWJONES_INDUSTRIAL = "DOWJONES_INDUSTRIAL"
    EURO_STOXX_50 = "EURO_STOXX_50"
    FTSE_100_INDEX = "FTSE_100_INDEX"
    HANG_SENG_CHINA_ENTERPRISES_INDEX = "HANG_SENG_CHINA_ENTERPRISES_INDEX"
    HO_CHI_MINH_STOCK_INDEX = "HO_CHI_MINH_STOCK_INDEX"
    NASDAQ_100 = "NASDAQ_100"
    NIKKEI_225_INDEX = "NIKKEI_225_INDEX"
    PHLX_SEMICONDUCTOR_S = "PHLX_SEMICONDUCTOR_S"
    RUSSELL_2000 = "RUSSELL_2000"
    SHANGHAI_COMPOSITE_INDEX = "SHANGHAI_COMPOSITE_INDEX"
    US_DOLLAR_INDEX = "US_DOLLAR_INDEX"
    MSCI_ACWI = "MSCI_ACWI"


class DefaultBenchmark:
    """
    A class that provides benchmark options and fetches benchmark data.

    This class includes a list of available benchmarks and methods to access and manipulate benchmark data.

    Attributes:
        available_list (list): A list of strings representing available benchmark options.

    Methods:
        available_options(): Returns the list of available benchmark options.
        get_benchmark_df(bench): Fetches and returns the benchmark data for the provided benchmark(s).
    """

    @classmethod
    def available_options(cls):
        """
        Returns the list of available benchmark options.

        Returns:
            list: A list of strings representing available benchmark options.
        """
        return [bm.value for bm in Benchmark]

    def get_benchmark_df(self, bench):
        """
        Fetches and returns the benchmark data for the provided benchmark(s).

        This method takes a benchmark identifier or a list of identifiers, converts them to uppercase,
        and retrieves their data. If a benchmark identifier includes a dot, it is left as is.

        Parameters:
            bench (str or list): A benchmark identifier or a list of identifiers.

        Returns:
            dict: A dictionary containing the benchmark data. Keys are benchmark identifiers, and values are pandas Series of percentage changes.
        """
        # Convert to list and uppercase if necessary
        if isinstance(bench, list):
            bench = [bm.upper() if "." not in bm else bm for bm in bench]
        elif isinstance(bench, str):
            bench = [bench.upper()] if not "." in bench else [bench]

        benchmarks = {}
        is_bm_models = []

        # Load benchmark data
        for bm in bench:
            bench_cm, is_bm_model = get_bench_cm(
                bm
            )  # Assuming this function is defined elsewhere
            is_bm_models.append(is_bm_model)
            if bm not in benchmarks.keys():
                if is_bm_model:
                    benchmarks[bench_cm] = Evaluator.get_cum_ret(
                        bench_cm, raw=True
                    )  # Assuming this method is defined elsewhere
                else:
                    loaded_data = ModelData.load(
                        bench_cm
                    )  # Assuming ModelData class is defined elsewhere
                    loaded_data.columns = loaded_data.columns.str.upper()
                    for key in bench:
                        if key in loaded_data.columns:
                            benchmarks[key] = loaded_data[key].pct_change()

        return benchmarks


class ModelUniverseConfig(Enum):
    KR_STOCK = {"benchmark": "KOSPI"}
    US_ETF = {"benchmark": "S&P500"}

    def get_config(self, model_type: ModelTypeConfig):
        if self == ModelUniverseConfig.KR_STOCK:
            return {
                "exchange": "krx",
                "universe": "krx",
                "instrument_type": "stock",
                "freq": "1d",
                "position_type": "target",
                "type": model_type.name.lower(),
                "exposure": "long_only",
            }
        elif self == ModelUniverseConfig.US_ETF:
            return {
                "exchange": "us",
                "universe": "compustat",
                "instrument_type": "etf",
                "freq": "1d",
                "position_type": "target",
                "type": model_type.name.lower(),
                "exposure": "long_only",
            }
        else:
            raise ValueError(f"Unknown universe: {self}")

    def get_benchmark_config(self, benchmark):
        if benchmark is None:
            return self.value["benchmark"]
        else:
            return benchmark

    @classmethod
    def available_options(cls):
        return ", ".join([item.name for item in cls])


def get_model_info(model_universe, model_type):
    try:
        model_info = ModelUniverseConfig[model_universe.upper()].get_config(
            model_type=ModelTypeConfig[model_type.upper()]
        )
    except KeyError:
        raise ValueError(
            f"Invalid model universe: {model_universe}. Available options: {ModelUniverseConfig.available_options()}"
        )

    return model_info


def get_output_path(model_name, model_type):
    return os.path.join(model_name, ModelTypeConfig[model_type.upper()].file_name)


def validate_and_get_model_type_name(model_type):
    try:
        model_type = ModelTypeConfig[model_type.upper()].name
    except KeyError:
        raise ValueError(
            f"Invalid model type: {model_type}. Available options: {ModelTypeConfig.available_options()}"
        )

    return model_type


def validate_and_get_benchmark_name(model_universe, benchmark):
    """
    Validates the given benchmark name against the available options for the specified model universe.

    This function checks if the provided benchmark name(s) exist within the available options for a given model universe.
    It also considers specific keywords that are allowed in the benchmark names.

    Args:
        model_universe (str): The name of the model universe to validate against.
        benchmark (str or list): The benchmark name or list of benchmark names to validate.

    Returns:
        str or list: The validated benchmark name(s).

    Raises:
        ValueError: If the benchmark name is invalid or the model universe is not found in the configuration.
    """

    def contains_keywords(s):
        """
        Checks if the given string contains any of the predefined keywords.

        Args:
            s (str): The string to check for keywords.

        Returns:
            bool: True if any keyword is found in the string, False otherwise.
        """
        keywords = ["alpha", "portfolio", "flexible_fund"]
        return any(keyword in s for keyword in keywords)

    available_options = DefaultBenchmark.available_options()
    try:
        # Retrieve benchmark configuration for the given model universe
        benchmark = ModelUniverseConfig[model_universe.upper()].get_benchmark_config(
            benchmark=benchmark
        )

        # Validate benchmark if it's a string
        if isinstance(benchmark, str):
            assert benchmark.upper() in available_options + [None] or contains_keywords(
                benchmark
            ), (
                f"Invalid benchmark: {benchmark}. Available options: "
                f"Submitted models or {available_options}, None"
            )
        # Validate benchmark if it's a list
        elif isinstance(benchmark, list):
            for bench in benchmark:
                assert bench.upper() in available_options + [None] or contains_keywords(
                    bench
                ), (
                    f"Invalid benchmark: {bench}. Available options: "
                    f"Submitted models or {available_options}, None"
                )
        else:
            raise KeyError
    except KeyError:
        # Raise ValueError if the model universe is not found or the benchmark is invalid
        raise ValueError(
            f"Invalid benchmark: {benchmark}. Available options: {available_options}"
        )

    return benchmark
