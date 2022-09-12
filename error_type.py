ERRORS = {
    0: "Unknown error.",
    # 1 scanner
    100: "",
    101: "Root dir path does not exist.",
    102: "Scan mode is invalid.",
    103: "Destination dir path does not exist.",
    # 2 doc item
    200: "",
    201: "Doc item's name should not be empty or null.",
    # 3 render
    300: "",
    301: "",
    # 4 custom list
    400: "",
    401: "Invalid item type.",
    405: "Key error: not exist.",
    406: "Key error: duplicate key.",
}


class ErrorType:
    def __init__(self, error_id):
        self.error_id = error_id
        if error_id not in ERRORS:
            self.error_id = 0
        self.error_name = ERRORS[self.error_id]
