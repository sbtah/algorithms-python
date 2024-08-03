class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        slow = self.head
        fast = self.head
        while True:
            slow = slow.next
            if slow.next is None:
                return False

            fast = fast.next.next
            if slow is fast:
                return True
            if fast is None:
                return False
            else:
                continue
                
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
my_linked_list_2.append(5)
print(my_linked_list_2.has_loop() ) # Returns False




[{'url': '/page.php?q=main', 'anchor': 'English'}, {'url': '/page.php?q=main&l=es', 'anchor': 'Español'}, {'url': '/page.php?q=main&l=de', 'anchor': 'Deutsch'}, {'url': '/page.php?q=main&l=fr', 'anchor': 'Français'}, {'url': '/page.php?q=main&l=it', 'anchor': 'Italiano'}, {'url': '/page.php?q=main&l=', 'anchor': ''}, {'url': 'http://kloshost.online/', 'anchor': 'kloshost.online'}, {'url': 'http:///', 'anchor': ''}, {'url': 'http://kloshost.i2p/?i2paddresshelper=jRzFU6J0WmMQt~JfOVOq4BT~XtXpohHETsxLJhnBF~oICvA-ioDSBrgvcG-L3NWlJtFP9dkcjBwvpb~r0~nLxJTLJCdnas0swMWLJY6SpVAyc7Dg4rdsF9d~9GM7HB35V4dXYnw5Wzxatr4stM5NYqquxvHnga7g5nLqLinJFaBuEEvM0j3tZK27pa7aoScI-SitMRc4bCh6QeMdhSsw3~UJwpdnJ7AyE7qfcqaXPSj~veOuU~uMlxmXxIjMPdZrPB3nYtfvmPrlCOXZTSL8ad8pD~JoPqTDhEKFJP~AJ6GIshsLYRxaGCZcFAmUtR4ssROOEYjcnR6MfXsAsdf3mi5EI6-wY~hEm4iaeRL-d53uCvmHTZu6ZN2tJT1TZ-PhIVQ70BR0m4OLvvOshHepGgDcCE8Cl21LTJGoJUYQ7an8KjhT~LxndP3qpgzYoxowirHmhjJ3~KiqbPFA~5ds-zys0Ky3LMtP7PPSVM9lve5ptLaL2HkJOMA6ko-iclEiBQAEAAEAAA==', 'anchor': 'kloshost.i2p'}, {'url': '/page.php', 'anchor': ''}, {'url': '/page.php?q=main', 'anchor': 'Main Page'}, {'url': '/page.php?q=services', 'anchor': 'Services'}, {'url': '/page.php?q=blog', 'anchor': 'Blog'}, {'url': '/page.php?q=prices', 'anchor': 'Price List'}, {'url': '/page.php?q=canary', 'anchor': 'Canary'}, {'url': '/page.php?q=about', 'anchor': 'About'}, {'url': '/page.php?q=user-policy', 'anchor': 'User Policy'}, {'url': '/page.php?q=guides', 'anchor': 'Guides'}, {'url': '/page.php?q=faq', 'anchor': 'FAQ'}, {'url': '/page.php?q=contact', 'anchor': 'Contact'}, {'url': '/page.php?q=accfaq', 'anchor': 'Account FAQ'}, {'url': '/page.php?q=hosting', 'anchor': 'Hosting'}, {'url': '/page.php?q=management', 'anchor': 'Service Management'}, {'url': '/page.php?q=relays', 'anchor': 'Relays'}, {'url': '/page.php?q=shell', 'anchor': 'Shell Accounts'}, {'url': '/page.php?q=viewpvs', 'anchor': 'ViewPVS vendor store'}, {'url': '/page.php?q=vps', 'anchor': 'Virtual Private Servers'}, {'url': '/page.php?q=main&b=system-disruption-2024jul08', 'anchor': 'Disruption for important update on 8th of July'}, {'url': 'http://forums.kaizushih5iec2mxohpvbt5uaapqdnbluaasa2cmsrrjtwrbx46cnaid.onion/index.php', 'anchor': 'KLOS Community Forum'}, {'url': 'http://klosforum.i2p/?i2paddresshelper=Ae7lJ88IVkH~okdE851~4OgmHTEgrTUB13A22eVjSGkB7uUnzwhWQf-iR0TznX~g6CYdMSCtNQHXcDbZ5WNIaQHu5SfPCFZB~6JHRPOdf-DoJh0xIK01AddwNtnlY0hpAe7lJ88IVkH~okdE851~4OgmHTEgrTUB13A22eVjSGkB7uUnzwhWQf-iR0TznX~g6CYdMSCtNQHXcDbZ5WNIaQHu5SfPCFZB~6JHRPOdf-DoJh0xIK01AddwNtnlY0hpAe7lJ88IVkH~okdE851~4OgmHTEgrTUB13A22eVjSGkB7uUnzwhWQf-iR0TznX~g6CYdMSCtNQHXcDbZ5WNIaQHu5SfPCFZB~6JHRPOdf-DoJh0xIK01AddwNtnlY0hpAe7lJ88IVkH~okdE851~4OgmHTEgrTUB13A22eVjSGkB7uUnzwhWQf-iR0TznX~g6CYdMSCtNQHXcDbZ5WNIaX8Tzz0cDYKu8bn8qM8OICB8eLCzvjqMDXhJLmKN6pV3BQAEAAcAAA==', 'anchor': 'i2p helper'}, {'url': 'http://juvenilezskkwc2gu7j5c4akppjnr3kzlgljjeodd5psn6fwcnloplid.onion/', 'anchor': 'Juvenile'}, {'url': 'http://forums.kaizushih5iec2mxohpvbt5uaapqdnbluaasa2cmsrrjtwrbx46cnaid.onion/index.php', 'anchor': 'my forum'}, {'url': 'https://libera.chat/', 'anchor': '#kloshost libera IRC channel'}, {'url': 'http://juvenilezskkwc2gu7j5c4akppjnr3kzlgljjeodd5psn6fwcnloplid.onion/', 'anchor': 'Juvenile IRC'}, {'url': '/page.php?q=contact', 'anchor': 'contact form'}, {'url': 'http://refuge3noitqegmmjericvur54ihyj7tsfyfwdblitaeaqu2koi7iuqd.onion/index.php?board=21.0', 'anchor': 'digital knowedge'}, {'url': 'http://juvenilezskkwc2gu7j5c4akppjnr3kzlgljjeodd5psn6fwcnloplid.onion/links.html', 'anchor': 'publish a little list of darknet links'}, {'url': '/page.php?q=contact', 'anchor': 'contact me via GPG'}, {'url': '/page.php?q=canary', 'anchor': 'check my canary'}, {'url': 'https://github.com/kaizushi/picosite', 'anchor': 'Picosite 1.2.3 (klos version)'}, {'url': '/template.php.txt', 'anchor': 'template file'}, {'url': '/page.php.txt', 'anchor': 'page.php.'}]