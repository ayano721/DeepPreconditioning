"""Configure file for training/testing PrecondNet."""

CFG = {
    'SEED': 42,
    'N_THREADS': 8,
    'DEVICE': 'cuda:0',  # or 'cpu'

    'DATA_ROOT': './data/',
    'DATA_COUNT': 1000,
    'PC_TRAIN': .50,  # train percent
    'PC_VAL': .25,  # validate percent, rest for testing
    'VALIDATE': True,
    'N_EPOCHS': 200,

    'LOAD_MODEL': './runs/trained_model.pt',
}
