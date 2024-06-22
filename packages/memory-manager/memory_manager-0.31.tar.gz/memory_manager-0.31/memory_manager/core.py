import threading
import time
from pymem import Pymem
from pymem.process import module_from_name
from pymem.exception import MemoryReadError, MemoryWriteError

class MemoryManager:
    def __init__(self):
        self.mem = None
        self.module = None
        self.triggers = []

    def hook(self, process_name, module_name, pointers):
        try:
            self.mem = Pymem(process_name)
            self.module = module_from_name(self.mem.process_handle, module_name).lpBaseOfDll
            self.read_funcs = {
                "4 Bytes": self.mem.read_int,
                "2 Bytes": self.mem.read_short,
                "Float": self.mem.read_float
            }
            self.write_funcs = {
                "4 Bytes": self.mem.write_int,
                "2 Bytes": self.mem.write_short,
                "Float": lambda address, value: self.mem.write_float(address, float(value))
            }
            self.add_get_set_functions(pointers)
            return pointers
        except Exception as e:
            print(f"Failed to hook process or module: {e}")
            return False

    def get_pointer_address(self, base, offsets):
        addr = self.mem.read_longlong(base)
        for offset in offsets:
            if offset != offsets[-1]:
                addr = self.mem.read_longlong(addr + offset)
        addr = addr + offsets[-1]
        return addr

    def get_value(self, address, data_type):
        try:
            if data_type in self.read_funcs:
                return self.read_funcs[data_type](address)
            else:
                raise ValueError(f"Unsupported type: {data_type}")
        except MemoryReadError:
            return False

    def set_value(self, address, data_type, value):
        try:
            if data_type in self.write_funcs:
                self.write_funcs[data_type](address, value)
                return True
            else:
                raise ValueError(f"Unsupported type: {data_type}")
        except MemoryWriteError:
            return False

    def add_get_set_functions(self, pointers):
        for key, value in pointers.items():
            if isinstance(value, dict) and "Address" in value and "Offsets" in value and "Type" in value:
                base_address = self.module + value["Address"]
                offsets = value["Offsets"]
                data_type = value["Type"]
                constant = value.get("Constant", True)

                if constant:
                    final_address = self.get_pointer_address(base_address, offsets)
                    value["Address"] = final_address
                    value["Get"] = lambda address=final_address, data_type=data_type: self.get_value(address, data_type)
                    value["Set"] = lambda new_value, address=final_address, data_type=data_type: self.set_value(address, data_type, new_value)
                else:
                    value["Get"] = lambda base_address=base_address, offsets=offsets, data_type=data_type: self.get_value(self.get_pointer_address(base_address, offsets), data_type)
                    value["Set"] = lambda new_value, base_address=base_address, offsets=offsets, data_type=data_type: self.set_value(self.get_pointer_address(base_address, offsets), data_type, new_value)
                
                # Adding Triggers
                value["Triggers"] = lambda frequency, func: self.add_trigger(value["Get"], frequency, func)
            elif isinstance(value, dict):
                self.add_get_set_functions(value)

    def add_trigger(self, get_func, frequency, callback):
        trigger = {
            "get_func": get_func,
            "frequency": frequency,
            "callback": callback,
            "active": True
        }
        thread = threading.Thread(target=self.monitor_value, args=(trigger,))
        thread.daemon = True
        thread.start()
        self.triggers.append(trigger)
        return lambda: self.remove_trigger(trigger)

    def remove_trigger(self, trigger):
        trigger["active"] = False

    def monitor_value(self, trigger):
        old_value = trigger["get_func"]()
        while trigger["active"]:
            time.sleep(trigger["frequency"])
            new_value = trigger["get_func"]()
            if new_value != old_value:
                trigger["callback"](old_value, new_value)
                old_value = new_value