# E2E-FS
E2E-FS: An End-to-End Feature Selection Method for Neural Networks

## CONTACT

This project is hosted at https://github.com/braisCB/E2E-FS. 

## REFERENCE

If you plan to use this code, please cite the following paper:

Cancela, B., Bolón-Canedo, V., & Alonso-Betanzos, A. (2020). 
E2E-FS: An End-to-End Feature Selection Method for Neural Networks. 
IEEE Transactions on Pattern Analysis and Machine Intelligence. *(Pending on publication)*

## EXAMPLE OF USE (for colon dataset)
    from dataset_reader import colon
    import numpy as np
    import e2efs
    
    
    n_features_to_select = 10
    
    if __name__ == '__main__':
    
        ## LOAD DATA
        dataset = colon.load_dataset()
        raw_data = np.asarray(dataset['raw']['data'])
        raw_label = np.asarray(dataset['raw']['label']).reshape(-1)
        train_data = raw_data[:int(len(raw_data) * 0.8)]
        train_label = raw_label[:int(len(raw_label) * 0.8)]
        test_data = raw_data[int(len(raw_data) * 0.8):]
        test_label = raw_label[int(len(raw_label) * 0.8):]
        normalize = colon.Normalize()
        train_data = normalize.fit_transform(train_data)
        test_data = normalize.transform(test_data)
    
        ## LOAD E2EFSSoft model
        model = e2efs.E2EFSSoft(n_features_to_select=n_features_to_select)
    
        ## OPTIONAL: Load E2EFS Model
        # model = e2efs.E2EFS(n_features_to_select=n_features_to_select)
    
        ## OPTIONAL: Load E2EFSRanking Model
        # model = e2efs.E2EFSRanking()
    
        ## FIT THE SELECTION
        model.fit(train_data, train_label, validation_data=(test_data, test_label), batch_size=2, max_epochs=2000)
    
        ## FINETUNE THE MODEL
        model.fine_tune(train_data, train_label, validation_data=(test_data, test_label), batch_size=2, max_epochs=100)
    
        ## GET THE MODEL RESULTS
        metrics = model.evaluate(test_data, test_label)
        print(metrics)
    
        ## GET THE MASK
        mask = model.get_mask()
        print('MASK:', mask)
    
        ## GET THE RANKING
        ranking = model.get_ranking()
        print('RANKING:', ranking)
    
    
