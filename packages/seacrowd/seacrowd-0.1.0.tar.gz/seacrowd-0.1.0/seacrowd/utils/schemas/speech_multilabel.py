"""
Speech Classification Schema for Multilabel
"""
import datasets

def features(label_names = ["Yes", "No"]):
    return datasets.Features(
        {
            "id": datasets.Value("string"),
            "path": datasets.Value("string"),
            "audio": datasets.Audio(sampling_rate=16_000),
            "speaker_id": datasets.Value("string"),
            "labels": datasets.Sequence(datasets.ClassLabel(names=label_names)),
            "metadata": {
                "speaker_age": datasets.Value("int64"),
                "speaker_gender": datasets.Value("string"),
            }
        }
    )
