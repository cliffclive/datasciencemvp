import src.data.make_dataset
import src.features.build_features
import src.models.train_model
import src.models.predict_model
import src.visualization.visualize

if __name__ == "__main__":
    src.data.make_dataset.run()
    src.features.build_features.run()
    src.models.train_model.run()
    src.models.predict_model.run()
    src.visualization.visualize.run()