# Описание проекта
Проект посвящен решеню задачи определения банковского кредитного скоринга клиента.

[Ссылка на исходную выборку данных ](https://www.kaggle.com/datasets/kapturovalexander/bank-credit-scoring/data)

Кредитный скоринг — это метод анализа, который банки и другие финансовые организации используют для оценки рисков при выдаче кредитов. Скоринговая оценка основывается на информации о кредитной истории клиента, его финансовом положении и других факторах

# Запуск
Для запуска проекта необходимо выполнить команды:
```
git clone https://github.com/yurchest/IIS_labs.git
cd {директория с проектом}
python3 -m venv .venv_IIS
source .venv_IIS/bin/activate
pip install -r requirements.txt
```

 Исследование данных

Находится в `./eda/eda.ipynb`. 

В ходе исследования были проведены действия:
* Удалены признаки "pdays","previous", "poutcome", так как не удалось обнаружить их теоретический и физический смысл
* В ходе анализа не было обнаружено аномальных значений признаков, противоречащих их физическому смыслу. Ни одна запись не была удалена.
* Столбцам 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'y' был присвоен категориальный тип
* Численныи столбцам ('age', 'balance', 'day', 'duration', 'campaign') был присвоен соответсвующий тип данных, подходящий под конкретный "разброс" значений

В ходе анализа были выявлены следующие закономерности: 
* В сфере менеджмента баланс клиента в среднем больше, а у студента баланс меньше. (график `./eda/graph1.png`)
* Наблюдаем слабую корелляцию признаков (график `./eda/graph2.png`)
* Для женатых клиентов процент отказов в выдаче кредита больше в сравнении с клиентами со статусом "в разводе" и "холост" (график `./eda/graph3.png`)
* Зависимость текущего баланса от возраста (график `./eda/graph4.png`)

Обработанная выборка сохранена в файл `./data/clean_data.pkl`