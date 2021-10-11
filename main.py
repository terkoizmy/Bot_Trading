import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("1a445ed5779c2f7633ec76ae32c65d9697da160118fdc57217b84448cd885941",
                            "30871da1f2e4f70557a9cdc621a1fece4449186dda43693a1335028645e46edd",
                            testnet=True, futures=True)
    bitmex = BitmexClient("8WQRYhSq0qamSkBnkzMk9QF0", "ZmHpW0gbQ2eBr0b89iiZPVbKMnvkvue69KeEGNDuhPllUu1I", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
