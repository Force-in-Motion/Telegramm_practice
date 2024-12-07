from Feedback.service.service import DataService as ds



class ListReview:
    def __init__(self):
        self.__reviews = ds.get_review()


    def add_review(self, id_user, name, grade, comment) -> None:
        """
        Создает отзыв пользователя в json файле в виде ключа, которым выступает id чата и списка строк в виде значения
        :param id_user: Принимает id чата
        :param name: Принимает название отзыва или чему он посвящен
        :param grade: Принимает оценку
        :param comment: Принимает комментарий
        :return:
        """
        data_review = f'Чему посвящен отзыв:\n{name}\nОценка: {grade}\nТекстовый комментарий:\n{comment}\n\n'

        id_user = str(id_user)

        if id_user not in self.__reviews:
            self.__reviews[id_user] = [data_review]

        else:
            self.__reviews[id_user].append(data_review)

        self.save()


    def save(self):
        """
        Сохраняет данные в файл json
        :return: None
        """
        ds.write_review(self.__reviews)





