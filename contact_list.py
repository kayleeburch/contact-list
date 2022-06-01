class ContactList():
    
    def __init__(self, group_name):
        self.group_name = group_name
        self.contacts = []
        
    def add_contact(self, name, number):
        dict = {}
        dict['name'] = name
        dict['number'] = number
        self.contacts.append(dict)
        sorted_contacts = sorted(self.contacts, key=lambda x: x['name'])
        self.contacts = sorted_contacts
    
    def remove_contact(self, name):
        for i in range(len(self.contacts)):
            if self.contacts[i]['name'] == name:
                del self.contacts[i]
                break
        
     
    def find_shared_contacts(self, check_contact):
        array = []
        for i in self.contacts:
            if i in check_contact.contacts:
                array.append(i)
        return array
                

def main():
    my_friends_list = ContactList('friends')
    my_friends_list.add_contact('Amy', '555-5555')
    my_friends_list.add_contact('chase', '333-3333')
    my_friends_list.add_contact('bob', '222-2222')
    # my_friends_list.remove_contact('Amy')
    print(my_friends_list.contacts)
    my_work_list = ContactList('work contacts')
    my_work_list.add_contact('john', '567-4356')
    my_work_list.add_contact('Amy', '555-5555')
    print(my_work_list.contacts)
    friends_i_work_with = my_friends_list.find_shared_contacts(my_work_list)
    print(friends_i_work_with)
    
    
    
if __name__ == '__main__':
    main()