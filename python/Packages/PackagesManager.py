import socket
def get_timer():
    return 10


class PackagesManager:
    a_available_packages: list # None ?
    _i_state_key: int  # iStateKey int.MIN_VALUE
    _i_last_package_length: int # range(0; 60 000)
    _i_last_package_type: int # int package
    _a_buffer: bytearray
    _i_last_time: int  # = get_timer()
    last_five_state_keys: list
    state_loop: int

    def process(self, socket):
        # if socket.
        #     return
        pass
