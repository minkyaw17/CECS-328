package com.EC5;

import java.lang.Math;
import java.util.Scanner;

class Node { // Node class
    int key;
    int height;
    Node left;
    Node right;

    Node (int val) {
        key = val;
        height = 1;
    }
}

class AVL {
    Node root;

    int height(Node n) {  // method to get height of tree
        if(n == null)
            return 0;

        return n.height;
    }

    int getBalanceFactor(Node n) {  // method to get the balance factor for rotations
        if (n == null)
            return 0;

        return height(n.left) - height(n.right);
    }

    Node leftRotation(Node z) {
        Node y = z.right;
        Node B = y.left;

        // rotation
        y.left = z;
        z.right = B;

        // updating height
        z.height = Math.max(height(z.left), height(z.right)) + 1;
        y.height = Math.max(height(y.left), height(y.right)) + 1;

        return y;
    }

    Node rightRotation(Node y) {
        Node x = y.left;
        Node B = x.right;

        // rotation
        x.right = y;
        y.left = B;

        // updating height
        y.height = Math.max(height(y.left), height(y.right)) + 1;
        x.height = Math.max(height(x.left), height(x.right)) + 1;

        return x;
    }

    Node insert(Node n, int key) {
        // BST insertions
        if (n == null) // if node is null, return a new node
            return new Node(key);

        if (key < n.key) // key is less so go the left
            n.left = insert(n.left, key);
        else if (key > n.key) // key is greater so it goes on the right
            n.right = insert(n.right, key);
        else // accounting for duplicates
            return n;

        n.height = Math.max(height(n.left), height(n.right)) + 1; // updating height

        int balanceFactor = getBalanceFactor(n); // getting balance factor of previous node to check if balanced/unbalanced

        if (balanceFactor > 1) {
            if (key < n.left.key)
                return rightRotation(n); // Left Left Rotation
            else if (key > n.left.key) {
                n.left = leftRotation(n.left);
                return rightRotation(n); // Left Right Rotation
            }
        }

        if (balanceFactor < -1) {
            if (key > n.right.key)
                return leftRotation(n); // Right Right Rotation
            else if (key < n.right.key) {
                n.right = rightRotation(n.right);
                return leftRotation(n); // Right Left Rotation
            }
        }

        return n;

    }

    void traverse(Node n) {
        if (n != null) {
            System.out.println(n.key);
            traverse(n.left);
            traverse(n.right);
        }
    }
}

public class Main {

    public static void main(String[] args) {
        AVL AVLTree = new AVL();

        Scanner in = new Scanner(System.in);
        System.out.println("Please enter numbers separated by white spaces:");
        String [] AVLArray = in.nextLine().split(" ");
        int [] AVLArraytoInt = new int[AVLArray.length];

        for (int i = 0; i < AVLArray.length; i++) {
            AVLArraytoInt[i] = Integer.parseInt(AVLArray[i]);
            AVLTree.root = AVLTree.insert(AVLTree.root, AVLArraytoInt[i]);
        }

        System.out.println("Traversed Tree:");
        AVLTree.traverse(AVLTree.root);

        in.close();
    }

}
