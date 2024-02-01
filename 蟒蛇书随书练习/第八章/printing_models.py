#printing_models.py
def printing_modles(unprint_models,printed_models):
    while unprint_models:
        printing = unprint_models.pop()
        print ("Now is printing ",printing)
        printed_models.append(printing)

def show_printed_moedls(printed_models):
    print ("The follow moedls are printed :")
    for model in printed_models:
        print (model)
        
unprint_models = ['A','B','C']
printed_models = []
printing_modles(unprint_models,printed_models)
show_printed_moedls(printed_models)