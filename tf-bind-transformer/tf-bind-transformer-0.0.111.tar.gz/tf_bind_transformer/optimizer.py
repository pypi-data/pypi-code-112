from torch.optim import AdamW

def separate_weight_decayable_params(params):
    no_wd_params = set([param for param in params if param.ndim < 2])
    wd_params = set(params) - no_wd_params
    return wd_params, no_wd_params

def get_optimizer(params, lr = 3e-4, wd = 1e-1, filter_by_requires_grad = False):
    if filter_by_requires_grad:
        params = list(filter(lambda t: t.requires_grad, params))

    params = set(params)
    wd_params, no_wd_params = separate_weight_decayable_params(params)

    param_groups = [
        {'params': list(wd_params)},
        {'params': list(no_wd_params), 'weight_decay': 0},
    ]

    return AdamW(param_groups, lr = lr, weight_decay = wd)
