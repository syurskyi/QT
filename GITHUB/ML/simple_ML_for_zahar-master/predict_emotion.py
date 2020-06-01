import os

from catboost import CatBoostClassifier
from pyAudioAnalysis import audioFeatureExtraction as At


def recognition_emotion_from_voice():
    classifier2 = CatBoostClassifier(iterations=1000, learning_rate=0.25,
                                     depth=5, loss_function='MultiClassOneVsAll',
                                     eval_metric="Accuracy")
    classifier2.load_model("stable_model")
    if len(os.listdir("data/voice/")) >= 3:
        data = At.dirsWavFeatureExtraction(["data/voice"], 1, 1, 0.05, 0.05)
        result = classifier2.predict(data[0][0])
        result = [x[0] for x in result]
        return max(result, key=result.count)
    return None


if __name__ == '__main__':
    print(recognition_emotion_from_voice())
