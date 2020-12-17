template <typename T>
struct tree {
    T value;
    tree* left;
    tree* right;
};

template <typename T, typename lesst>tree<T>* find (tree<T>* t, T item, lesst less) {   if(less(item,t->value)){      return find(t->left,less);   } else if(!less(t->value, item)) {      return t;   } else {      return find(t->right,less);   }}