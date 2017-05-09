from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import AverageDollarVolume
from quantopian.pipeline.filters.morningstar import Q1500US

def initialize(context):
    """
    Set up algorithm.
    """
    # Create our dynamic stock selector.
    attach_pipeline(make_pipeline(), 'my_pipeline')

def handle_data(context, data):
    """
    Process data every minute.
    """
    pass

def before_trading_start(context, data):
    """
    Define universe before every market open.
    """
    context.output = pipeline_output('my_pipeline')

    # These are the securities that we are interested in trading each day.
    context.security_list = context.output.index

def make_pipeline():
    """
    A function to create our dynamic stock selector (pipeline). Documentation on
    pipeline can be found here: https://www.quantopian.com/help#pipeline-title
    """
    # Base universe set to the Q500US
    base_universe = Q1500US()

    # Factor of yesterday's close price.
    yesterday_close = USEquityPricing.close.latest

    pipe = Pipeline(
        screen = base_universe,
        columns = {
            'close': yesterday_close,
        }
    )
    return pipe