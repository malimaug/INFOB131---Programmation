import os
os.chdir('EX4')


structure_isbn = {'123-0000000001': {'authors': ('Paolini Christopher', 'Mull Brandon'),
                                     'nbr_pages': 123,
                                     'year': 2010},

                  '123-0000000002': {'authors': ('Paolini Christopher',),
                                     'nbr_pages': 256,
                                     'year': 2011},

                  '123-0000000003': {'authors': ('Paolini Christopher',),
                                     'nbr_pages': 512,
                                     'year': 2012},

                  '123-0000000004': {'authors': ('Nothomb Amelie',),
                                     'nbr_pages': 1024,
                                     'year': 2013},

                  '123-0000000005': {'authors': ('Nothomb Amelie',),
                                     'nbr_pages': 2048,
                                     'year': 2014},

                  '123-0000000006': {'authors': ('Nothomb Amelie',),
                                     'nbr_pages': 128,
                                     'year': 2015},
                  '123-0000000007': {'authors': ('Collins Suzanne',),
                                     'nbr_pages': 64,
                                     'year': 2016},

                  '123-0000000008': {'authors': ('Collins Suzanne',),
                                     'nbr_pages': 32,
                                     'year': 2017},

                  '123-0000000009': {'authors': ('Collins Suzanne',),
                                     'nbr_pages': 16,
                                     'year': 2018},

                  '123-0000000010': {'authors': ('Paolini Christopher','Mull Brandon'),
                                     'nbr_pages': 8,
                                     'year': 2019},
                  }

structure_authors = {'Paolini Christopher': ['123-0000000001', '123-0000000002', '123-0000000003'],
                     'Nothomb Amelie': ['123-0000000004', '123-0000000005', '123-0000000006'],
                     'Collins Suzanne': ['123-0000000007', '123-0000000008', '123-0000000009'],
                     'Mull Brandon': ['123-0000000010', '123-0000000001'],
                     }


for author in structure_authors:

    os.mkdir(author)
    
    for isbn in structure_authors[author]:

        book_file = open('%s/%s.book' % (author, isbn), 'w')

        file_content = "Nombre de pages : %d \nAnnée de parution : %d" % (structure_isbn[isbn]['nbr_pages'], structure_isbn[isbn]['year'])

        book_file.write(file_content)

        book_file.close()