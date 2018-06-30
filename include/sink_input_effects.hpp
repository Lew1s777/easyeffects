#ifndef SINK_INPUT_EFFECTS_HPP
#define SINK_INPUT_EFFECTS_HPP

#include "bass_enhancer.hpp"
#include "compressor.hpp"
#include "crossfeed.hpp"
#include "deesser.hpp"
#include "delay.hpp"
#include "equalizer.hpp"
#include "exciter.hpp"
#include "filter.hpp"
#include "gate.hpp"
#include "limiter.hpp"
#include "loudness.hpp"
#include "maximizer.hpp"
#include "multiband_compressor.hpp"
#include "multiband_gate.hpp"
#include "panorama.hpp"
#include "pipeline_base.hpp"
#include "pulse_manager.hpp"
#include "reverb.hpp"
#include "stereo_enhancer.hpp"

class SinkInputEffects : public PipelineBase {
   public:
    SinkInputEffects(PulseManager* pulse_manager);
    virtual ~SinkInputEffects();

    std::string log_tag;

    PulseManager* pm;

    std::vector<std::string> plugins_order, plugins_order_old;
    std::map<std::string, GstElement*> plugins;

    std::unique_ptr<Limiter> limiter;
    std::unique_ptr<Compressor> compressor;
    std::unique_ptr<Filter> filter;
    std::unique_ptr<Equalizer> equalizer;
    std::unique_ptr<Reverb> reverb;
    std::unique_ptr<BassEnhancer> bass_enhancer;
    std::unique_ptr<Exciter> exciter;
    std::unique_ptr<StereoEnhancer> stereo_enhancer;
    std::unique_ptr<Panorama> panorama;
    std::unique_ptr<Crossfeed> crossfeed;
    std::unique_ptr<Maximizer> maximizer;
    std::unique_ptr<Delay> delay;
    std::unique_ptr<MultibandCompressor> multiband_compressor;
    std::unique_ptr<Loudness> loudness;
    std::unique_ptr<Gate> gate;
    std::unique_ptr<MultibandGate> multiband_gate;
    std::unique_ptr<Deesser> deesser;

    sigc::signal<void, std::array<double, 2>> compressor_input_level;
    sigc::signal<void, std::array<double, 2>> compressor_output_level;
    sigc::signal<void, std::array<double, 2>> equalizer_input_level;
    sigc::signal<void, std::array<double, 2>> equalizer_output_level;
    sigc::signal<void, std::array<double, 2>> bass_enhancer_input_level;
    sigc::signal<void, std::array<double, 2>> bass_enhancer_output_level;
    sigc::signal<void, std::array<double, 2>> exciter_input_level;
    sigc::signal<void, std::array<double, 2>> exciter_output_level;
    sigc::signal<void, std::array<double, 2>> panorama_input_level;
    sigc::signal<void, std::array<double, 2>> panorama_output_level;
    sigc::signal<void, std::array<double, 2>> crossfeed_input_level;
    sigc::signal<void, std::array<double, 2>> crossfeed_output_level;
    sigc::signal<void, std::array<double, 2>> maximizer_input_level;
    sigc::signal<void, std::array<double, 2>> maximizer_output_level;
    sigc::signal<void, std::array<double, 2>> delay_input_level;
    sigc::signal<void, std::array<double, 2>> delay_output_level;
    sigc::signal<void, std::array<double, 2>> loudness_input_level;
    sigc::signal<void, std::array<double, 2>> loudness_output_level;
    sigc::signal<void, std::array<double, 2>> gate_input_level;
    sigc::signal<void, std::array<double, 2>> gate_output_level;
    sigc::signal<void, std::array<double, 2>> deesser_input_level;
    sigc::signal<void, std::array<double, 2>> deesser_output_level;

   private:
    GSettings* sie_settings;

    void add_plugins_to_pipeline();

    void on_app_added(const std::shared_ptr<AppInfo>& app_info);
};

#endif
