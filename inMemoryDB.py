__author__ = 'kathan'
from uuid import uuid4

DATABASE = {}  # main source of storage
COUNT_DB = {}  # main source of count values

TRANSACTION_STACK = []  # transaction stack with uuid

UNCOMMITED_DATABASE = {}  # uncommited data per transaction
UNCOMMITED_COUNT_DB = {}  # uncommited count data per transaction



# sets value in database and updates COUNT_DB
def set_value(key, value, transaction=None):
    if transaction:
        if key in UNCOMMITED_DATABASE[transaction]:
            #get the count of current key and subtract 1
            count_key = UNCOMMITED_DATABASE[transaction][key]
            if UNCOMMITED_COUNT_DB[transaction][count_key] > 0:
                UNCOMMITED_COUNT_DB[transaction][count_key] = UNCOMMITED_COUNT_DB[transaction][count_key] - 1
            else:
                UNCOMMITED_COUNT_DB[transaction][count_key] = 0

            UNCOMMITED_DATABASE[transaction][key] = value
            if value in UNCOMMITED_COUNT_DB[transaction]:
                UNCOMMITED_COUNT_DB[transaction][value] = UNCOMMITED_COUNT_DB[transaction][value] + 1
            else:
                UNCOMMITED_COUNT_DB[transaction][value] = 1
        else:
            UNCOMMITED_DATABASE[transaction][key] = value
            if value in UNCOMMITED_COUNT_DB[transaction]:
                UNCOMMITED_COUNT_DB[transaction][value] = UNCOMMITED_COUNT_DB[transaction][value] + 1
            else:
                UNCOMMITED_COUNT_DB[transaction][value] = 1

    else:
        if key in DATABASE:
            #get the count of current key and subtract 1
            count_key = DATABASE[key]
            COUNT_DB[count_key] = COUNT_DB[count_key] - 1 if COUNT_DB[count_key] > 0 else 0

            DATABASE[key] = value
            if value in COUNT_DB:
                COUNT_DB[value] = COUNT_DB[value] + 1
            else:
                COUNT_DB[value] = 1
        else:
            DATABASE[key] = value
            if value in COUNT_DB:
                COUNT_DB[value] = COUNT_DB[value] + 1
            else:
                COUNT_DB[value] = 1


# gets value from database if key is present else returns null
def get_value(key, transaction=None):
    if transaction:
        if key in UNCOMMITED_DATABASE[transaction]:
            return UNCOMMITED_DATABASE[transaction][key]
        else:
            if key in DATABASE:
                return DATABASE[key]
            else:
                return None
    else:
        if key in DATABASE:
            return DATABASE[key]
        else:
            return None


# deletes key from database if exists and update COUNT_DB
def delete_key(key, transaction=None):
    if transaction:
        if key in UNCOMMITED_DATABASE[transaction]:
            UNCOMMITED_COUNT_DB[transaction][UNCOMMITED_DATABASE[transaction][key]] = UNCOMMITED_COUNT_DB[transaction][UNCOMMITED_DATABASE[transaction][key]] - 1
            del UNCOMMITED_DATABASE[transaction][key]
    else:
        if key in DATABASE:
            COUNT_DB[DATABASE[key]] = COUNT_DB[DATABASE[key]] - 1
            del DATABASE[key]


# returns the count of the number of occurance of the key
def get_count(value, transaction=None):
    if transaction:
        total_count = get_count(value)

        for trans in TRANSACTION_STACK:
            if value in UNCOMMITED_COUNT_DB[trans]:
                total_count = total_count + UNCOMMITED_COUNT_DB[trans][value]
            if trans == transaction:
                break

        return total_count
    else:
        if value in COUNT_DB:
            return COUNT_DB[value]
        else:
            return 0


# starts transaction which one can roll back
def start_transaction():
    transaction_hash = uuid4()

    TRANSACTION_STACK.append(transaction_hash)

    UNCOMMITED_DATABASE[transaction_hash] = {}
    UNCOMMITED_COUNT_DB[transaction_hash] = {}

    return transaction_hash


def commit_data():
    uncommitted_data = {}
    uncommited_count_data = {}

    for trans in TRANSACTION_STACK:
        uncommitted_data.update(UNCOMMITED_DATABASE[trans])
        uncommited_count_data.update(UNCOMMITED_COUNT_DB[trans])

    DATABASE.update(uncommitted_data)# A.update(B)
    COUNT_DB.update(uncommited_count_data)


def rollback_data():
    transaction_value = TRANSACTION_STACK.pop()
    del UNCOMMITED_COUNT_DB[transaction_value]
    del UNCOMMITED_DATABASE[transaction_value]



def test_case_just_get_set_count():
    set_value('a', 10)
    set_value('b', 10)
    print get_count(10)
    print get_count(20)

    delete_key('a')
    print get_count(10)

    set_value('b', 30)
    print get_count(10)
    print get_count(30)
    print get_count(20)


def test_case_for_transaction():
    # transaction cases
    transaction_value_a = start_transaction()
    set_value('a', 10, transaction_value_a)
    print get_value('a', transaction_value_a)

    transaction_value_b = start_transaction()
    set_value('a', 20, transaction_value_b)
    print get_value('a', transaction_value_b)
    rollback_data()

    print get_value('a', transaction_value_a)

    rollback_data()

    print get_value('a')


def test_case_for_transaction_count():
    set_value('a', 10)

    trans_a = start_transaction()
    print get_count(10, trans_a)

    trans_b = start_transaction()
    delete_key('a', trans_b)

    print get_count(10, trans_b)

    rollback_data()

    print get_count(10, trans_a)


if __name__ == "__main__":
    #test_case_just_get_set_count()

    #test_case_for_transaction()

    test_case_for_transaction_count()
