from models.model import train_model
from models.run_game import train

updated_model, y, result = train(train_model(), mode="Hard", print_progress=True)

updated_model.save('model.h5')