from gtts import gTTS

def narrate(text,  language = 'es', output_filename = None):
    """
    Creates an audio narration of the provided 'text' with the Google voice and stores it
    as 'output_filename'. This will use the provided 'language' language for the narration.
    """
    if not output_filename:
        return None
    
    # TODO: Check valid language tag in this table (https://en.wikipedia.org/wiki/IETF_language_tag)
    # TODO: Use this library for languages (https://pypi.org/project/langcodes/)
    tts = gTTS(text, lang = language)
    tts.save(output_filename)