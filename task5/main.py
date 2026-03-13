from src.table_a import load_table_a
from src.table_b import load_table_b
from src.table_c import load_table_c

def main():

    print("A)")
    load_table_a()
    print("B)")
    print("="*80)
    load_table_b()
    print("C)")
    print("="*80)
    load_table_c()

if __name__ == "__main__":
    main()