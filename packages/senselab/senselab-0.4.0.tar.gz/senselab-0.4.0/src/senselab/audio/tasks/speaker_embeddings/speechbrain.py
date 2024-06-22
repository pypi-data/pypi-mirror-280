"""Provides a factory for extracting speaker embeddings from a list of audios using speechbrain."""

from typing import Dict, List, Optional

import torch
from speechbrain.inference.speaker import EncoderClassifier

from senselab.audio.data_structures.audio import Audio
from senselab.utils.data_structures.device import DeviceType, _select_device_and_dtype
from senselab.utils.data_structures.model import HFModel


class SpeechBrainEmbeddings:
    """A factory for extracting speaker embeddings using speechbrain models."""

    _models: Dict[str, EncoderClassifier] = {}

    @classmethod
    def _get_speechbrain_model(
        cls,
        model: HFModel,
        device: Optional[DeviceType] = None,
    ) -> EncoderClassifier:
        """Get or create a SpeechBrain model.

        Args:
            model (HFModel): The SpeechBrain model.
            device (Optional[DeviceType]): The device to run the model on.
                Only CPU and CUDA are supported.

        Returns:
            EncoderClassifier: The SpeechBrain model.

        Todo:
            - Adding savedir for storing models
        """
        device, _ = _select_device_and_dtype(
            user_preference=device, compatible_devices=[DeviceType.CUDA, DeviceType.CPU]
        )
        key = f"{model.path_or_uri}-{model.revision}-{device.value}"
        if key not in cls._models:
            cls._models[key] = EncoderClassifier.from_hparams(
                source=model.path_or_uri, run_opts={"device": device.value}
            )
        return cls._models[key]

    @classmethod
    def extract_speechbrain_speaker_embeddings_from_audios(
        cls,
        audios: List[Audio],
        model: HFModel = HFModel(path_or_uri="speechbrain/spkrec-ecapa-voxceleb", revision="main"),
        device: Optional[DeviceType] = None,
    ) -> List[torch.Tensor]:
        """Compute the speaker embeddings of audio signals.

        Args:
            audios (List[Audio]): A list of Audio objects containing the audio signals and their properties.
            model (HFModel): The model used to compute the embeddings (default is "speechbrain/spkrec-ecapa-voxceleb").
            device (Optional[DeviceType]): The device to run the model on (default is None).
                Only CPU and CUDA are supported.

        Returns:
            List[torch.Tensor]: A list of tensors containing the speaker embeddings for each audio file.
        """
        classifier = cls._get_speechbrain_model(model=model, device=device)

        # Stack audio waveforms for batch processing
        waveforms = torch.stack([audio.waveform for audio in audios]).squeeze()

        # Compute embeddings in a batch
        embeddings_batch = classifier.encode_batch(waveforms)

        # Split the batch embeddings into a list of individual embeddings
        embeddings = [embedding.squeeze() for embedding in embeddings_batch]

        return embeddings
