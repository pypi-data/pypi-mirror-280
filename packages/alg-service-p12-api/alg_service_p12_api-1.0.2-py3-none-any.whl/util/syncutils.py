import os



from util.utils import get_user_home, remove_file


def locked( lock = None):

    def real_lock(func):
        def wrapper(self, *args, **kwargs):
            lockobj = getattr(self, lock)
            with lockobj:
                return func(self, *args, **kwargs)

        return wrapper

    return real_lock



def clean_and_save_user_spec_file( filename , content ):
    home = get_user_home()
    fullfile = os.path.join(home, filename)
    remove_file(fullfile);

    with open(fullfile, 'w') as f:
        f.write(str(content))

def read_user_spec_file( filename  ):
    home = get_user_home()
    fullfile = os.path.join(home, filename)
    try:
        with open(fullfile, 'r') as f:
            line = f.readline()
            return line
    except Exception as e:
        print("read file error ", fullfile ,e )
    return None


