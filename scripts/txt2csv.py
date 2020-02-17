import csv

for i in range(2016, 2017, 2):

    with open('../data/CampaignFinanceData/CFD'+str(i)+'/cands'+str(i)[2:]+'.txt', newline = '') as txtfile:
        reader = csv.reader(txtfile, quotechar='|')

        with open('../data/CampaignFinanceData/CFD'+str(i)+'/cands'+str(i)[2:]+'.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in reader:
                writer.writerow(row)

    with open('../data/CampaignFinanceData/CFD'+str(i)+'/cmtes'+str(i)[2:]+'.txt', newline = '', errors = 'ignore') as txtfile:
        reader = csv.reader(txtfile, quotechar='|')

        with open('../data/CampaignFinanceData/CFD'+str(i)+'/cmtes'+str(i)[2:]+'.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in reader:
                writer.writerow(row)

    with open('../data/CampaignFinanceData/CFD'+str(i)+'/indivs'+str(i)[2:]+'.txt', newline = '', errors = 'ignore') as txtfile:
        reader = csv.reader(txtfile, quotechar='|')

        with open('../data/CampaignFinanceData/CFD'+str(i)+'/indivs'+str(i)[2:]+'.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in reader:
                writer.writerow(row)

    with open('../data/CampaignFinanceData/CFD'+str(i)+'/pac_other'+str(i)[2:]+'.txt', newline = '') as txtfile:
        reader = csv.reader(txtfile, quotechar='|')

        with open('../data/CampaignFinanceData/CFD'+str(i)+'/pac_other'+str(i)[2:]+'.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in reader:
                writer.writerow(row)

    with open('../data/CampaignFinanceData/CFD'+str(i)+'/pacs'+str(i)[2:]+'.txt', newline = '') as txtfile:
        reader = csv.reader(txtfile, quotechar='|')

        with open('../data/CampaignFinanceData/CFD'+str(i)+'/pacs'+str(i)[2:]+'.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in reader:
                writer.writerow(row)