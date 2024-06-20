from call_sequencer import CallSequencer


@CallSequencer.simple
def simple_func(param):
    # operation
    return param


@CallSequencer.with_args
def with_args_func(param1, *args):
    # operation
    return "res" + param1 + "".join(args)


def test_main():
    seq = CallSequencer.start("Hello") >> simple_func >> with_args_func(" ","World")

    print(seq())

test_main()