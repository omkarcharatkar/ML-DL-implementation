from MLlib.models import LinearRegression, LogisticRegression
from MLlib.optimizers import Adam, GradientDescent
from MLlib.loss_func import MeanSquaredError, LogarithmicError
from MLlib.utils import read_data, printmat


X, Y = read_data('MLlib/datasets/logistic_reg_00.txt')

logistic_model = LogisticRegression()

optimizer = GradientDescent(0.05, LogarithmicError)

logistic_model.fit(X, Y, optimizer=optimizer, epochs=200, zeros=False)

printmat('predictions', logistic_model.predict(X))

logistic_model.save('test')