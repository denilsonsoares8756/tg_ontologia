from app.ml.model import predict_model
from app.ontology.reasoner import enrich_with_ontology

def run_pipeline(data):
    # 1. Predição ML
    prediction = predict_model(data)

    # 2. Pós-processamento ontológico
    enriched = enrich_with_ontology(prediction)

    return {
        "raw_prediction": prediction,
        "enriched_prediction": enriched
    }