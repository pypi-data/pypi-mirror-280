from TTS.api import TTS

# TODO: From here (https://github.com/coqui-ai/TTS)
def narrate(text, output_filename = None):
    if not output_filename:
        return None
    
    # tts_es_fastpitch_multispeaker.nemo
    # These below are the 2 Spanish models that exist
    SPANISH_MODEL_A = 'tts_models/es/mai/tacotron2-DDC'
    SPANISH_MODEL_B = 'tts_models/es/css10/vits'
    tts = TTS(model_name = SPANISH_MODEL_B)
    tts.tts_to_file(text = text, file_path = output_filename)