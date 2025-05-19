import platform

if platform.system() == "Windows":
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))

    def set_volume(percent):
        vol = max(0.0, min(1.0, percent / 100.0))
        volume_interface.SetMasterVolumeLevelScalar(vol, None)

elif platform.system() == "Darwin":
    import os

    def set_volume(percent):
        vol = int(max(0, min(100, percent)))
        os.system(f"osascript -e 'set volume output volume {vol}'")

elif platform.system() == "Linux":
    import os

    def set_volume(percent):
        vol = int(max(0, min(100, percent)))
        os.system(f"pactl set-sink-volume @DEFAULT_SINK@ {vol}%")

else:
    def set_volume(percent):
        print(f"[!] Set volume not supported on {platform.system()}")
