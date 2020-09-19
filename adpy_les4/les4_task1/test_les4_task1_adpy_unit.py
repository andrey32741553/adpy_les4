from adpy_les4.les4_task1.les4adpy import documents, show_list_of_doc, add_new_data, del_doc_by_num
import unittest


class Test_les5_task1(unittest.TestCase):

    def setUp(self):
        print('method setup')


    def tearDown(self):
        print('method teardown')


    def test_show_list_of_doc(self):
        result_list = []
        for line in documents:
            result_list.append(f'{line["type"]} {line["number"]} {line["name"]}')
        self.assertEqual(show_list_of_doc(), result_list)


    def testing_add_new_data_doc(self):
        info_from_add_new_data = add_new_data()
        self.assertEqual(info_from_add_new_data[0][3]['number'], '0945 564783')
        self.assertEqual(info_from_add_new_data[1]['3'], ['0945 564783'])


    def testing_del_doc_by_num(self):
        self.assertNotIn('2207 876234', del_doc_by_num())
