# -*- coding: utf-8 -*-

import configparser

from gi.repository import GLib
from PulseEffects.bass_enhancer_presets import BassEnhancerPresets
from PulseEffects.compressor_presets import CompressorPresets
from PulseEffects.crossfeed_presets import CrossfeedPresets
from PulseEffects.delay_presets import DelayPresets
from PulseEffects.equalizer_presets import EqualizerPresets
from PulseEffects.exciter_presets import ExciterPresets
from PulseEffects.gate_presets import GatePresets
from PulseEffects.highpass_presets import HighpassPresets
from PulseEffects.limiter_presets import LimiterPresets
from PulseEffects.lowpass_presets import LowpassPresets
from PulseEffects.maximizer_presets import MaximizerPresets
from PulseEffects.output_limiter_presets import OutputLimiterPresets
from PulseEffects.panorama_presets import PanoramaPresets
from PulseEffects.pitch_presets import PitchPresets
from PulseEffects.reverb_presets import ReverbPresets
from PulseEffects.stereo_enhancer_presets import StereoEnhancerPresets
from PulseEffects.stereo_spread_presets import StereoSpreadPresets


class LoadPresets():

    def __init__(self):
        self.config = configparser.ConfigParser()

        self.limiter_presets = LimiterPresets(self.config)
        self.panorama_presets = PanoramaPresets(self.config)
        self.compressor_presets = CompressorPresets(self.config)
        self.reverb_presets = ReverbPresets(self.config)
        self.highpass_presets = HighpassPresets(self.config)
        self.lowpass_presets = LowpassPresets(self.config)
        self.equalizer_presets = EqualizerPresets(self.config)
        self.exciter_presets = ExciterPresets(self.config)
        self.bass_enhancer_presets = BassEnhancerPresets(self.config)
        self.delay_presets = DelayPresets(self.config)
        self.stereo_enhancer_presets = StereoEnhancerPresets(self.config)
        self.stereo_spread_presets = StereoSpreadPresets(self.config)
        self.crossfeed_presets = CrossfeedPresets(self.config)
        self.maximizer_presets = MaximizerPresets(self.config)
        self.output_limiter_presets = OutputLimiterPresets(self.config)
        self.pitch_presets = PitchPresets(self.config)
        self.gate_presets = GatePresets(self.config)

    def set_config_path(self, path):
        self.config.clear()
        self.config.read(path)

    def load_deesser_preset(self, settings, section):
        enabled = self.config.getboolean(section, 'enabled', fallback=False)
        detection = self.config.getboolean(section, 'detection_type_rms',
                                           fallback=True)
        mode = self.config.getboolean(section, 'mode_type_wide', fallback=True)
        threshold = self.config.getfloat(section, 'threshold', fallback=-18.0)
        ratio = self.config.getfloat(section, 'ratio', fallback=3.0)
        makeup = self.config.getfloat(section, 'makeup', fallback=0.0)
        laxity = self.config.getint(section, 'laxity', fallback=15)
        f1 = self.config.getfloat(section, 'f1', fallback=6000.0)
        f1_level = self.config.getfloat(section, 'f1_level', fallback=0.0)
        f2 = self.config.getfloat(section, 'f2', fallback=4500.0)
        f2_level = self.config.getfloat(section, 'f2_level', fallback=12.0)
        f2_q = self.config.getfloat(section, 'f2_q', fallback=1.0)

        settings.set_value('deesser-state', GLib.Variant('b', enabled))
        settings.set_value('deesser-detection-rms',
                           GLib.Variant('b', detection))
        settings.set_value('deesser-mode-wide', GLib.Variant('b', mode))
        settings.set_value('deesser-threshold', GLib.Variant('d', threshold))
        settings.set_value('deesser-ratio', GLib.Variant('d', ratio))
        settings.set_value('deesser-makeup', GLib.Variant('d', makeup))
        settings.set_value('deesser-laxity', GLib.Variant('i', laxity))
        settings.set_value('deesser-f1', GLib.Variant('d', f1))
        settings.set_value('deesser-f1-level', GLib.Variant('d', f1_level))
        settings.set_value('deesser-f2', GLib.Variant('d', f2))
        settings.set_value('deesser-f2-level', GLib.Variant('d', f2_level))
        settings.set_value('deesser-f2-q', GLib.Variant('d', f2_q))

    def load_source_outputs_preset(self, settings):
        self.load_deesser_preset(settings, 'mic_deesser')

    def load(self):
        self.limiter_presets.load()
        self.panorama_presets.load()
        self.compressor_presets.load()
        self.reverb_presets.load()
        self.highpass_presets.load()
        self.lowpass_presets.load()
        self.equalizer_presets.load()
        self.exciter_presets.load()
        self.bass_enhancer_presets.load()
        self.delay_presets.load()
        self.stereo_enhancer_presets.load()
        self.stereo_spread_presets.load()
        self.crossfeed_presets.load()
        self.maximizer_presets.load()
        self.output_limiter_presets.load()
        self.pitch_presets.load()
        self.gate_presets.load()
