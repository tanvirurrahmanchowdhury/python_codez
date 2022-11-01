from fireworks import LaunchPad

fw_ids = input("Enter the fw id: ")
lpad = LaunchPad.auto_load()
fw_dict = lpad.get_fw_dict_by_id(int(fw_ids))
error_message = fw_dict['launches'][0]["action"]['stored_data']['_exception']['_stacktrace']
print(error_message)
