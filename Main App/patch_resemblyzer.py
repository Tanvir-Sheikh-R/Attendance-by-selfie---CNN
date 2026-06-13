import sys
import types

# Fake webrtcvad module to avoid pkg_resources error
fake_webrtcvad = types.ModuleType("webrtcvad")

class Vad:
    def __init__(self, mode=3): pass
    def is_speech(self, buf, sample_rate): return True

fake_webrtcvad.Vad = Vad
sys.modules["webrtcvad"] = fake_webrtcvad