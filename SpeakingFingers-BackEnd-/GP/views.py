from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AudioFileSerializer
from .tasks import speech_to_text, text_to_phonetic
from .detailed_similarity_analysis import detailed_similarity_analysis_and_feedback

class SpeechAnalysisView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AudioFileSerializer(data=request.data)
        if serializer.is_valid():
            audio_file = serializer.validated_data['audio_file']
            # Assuming audio_file is a path or file-like object compatible with your speech_to_text function
            text_output = speech_to_text(audio_file)
            phonetic_output = text_to_phonetic(text_output)
            # You would also need to handle the reference text input, potentially as another field in your serializer
            # For simplicity, this example assumes it's provided or hardcoded
            reference_text = "your reference text here"
            ref_phonetic = text_to_phonetic(reference_text)
            similarity, errors, feedback = detailed_similarity_analysis_and_feedback(ref_phonetic, phonetic_output)
            return Response({
                "text_output": text_output,
                "phonetic_output": phonetic_output,
                "similarity_score": similarity,
                "errors": errors,
                "feedback": feedback
            })
        return Response(serializer.errors, status=400)
