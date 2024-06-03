import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { fetchProducts, createProduct, updateProduct, deleteProduct } from '../services/productService';
import { Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';

const columns = [
  { field: 'id', headerName: 'ID', width: 90, editable: false },
  { field: 'name', headerName: 'Name', width: 150, editable: true },
  { field: 'description', headerName: 'Description', width: 250, editable: true },
  { field: 'price', headerName: 'Price', type: 'number', width: 120, editable: true },
  { field: 'quantity', headerName: 'Quantity', type: 'number', width: 120, editable: true },
];

export default function ProductDataGrid() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [open, setOpen] = useState(false);
  const [newProduct, setNewProduct] = useState({ name: '', description: '', price: '', quantity: '' });

  useEffect(() => {
    async function loadData() {
      const data = await fetchProducts();
      setProducts(data);
      setLoading(false);
    }
    loadData();
  }, []);

  const handleProcessRowUpdate = async (newRow) => {
    const updatedProduct = await updateProduct(newRow.id, newRow);
    setProducts((prev) => prev.map((row) => (row.id === newRow.id ? updatedProduct : row)));
    return updatedProduct;
  };

  const handleDeleteClick = async (id) => {
    await deleteProduct(id);
    setProducts((prev) => prev.filter((row) => row.id !== id));
  };

  const handleAddClick = async () => {
    const createdProduct = await createProduct(newProduct);
    setProducts((prev) => [...prev, createdProduct]);
    setNewProduct({ name: '', description: '', price: '', quantity: '' });
    setOpen(false);
  };

  const renderDeleteButton = (params) => {
    return (
      <Button variant="contained" color="secondary" onClick={() => handleDeleteClick(params.id)}>
        Delete
      </Button>
    );
  };

  const columnsWithDelete = [
    ...columns,
    {
      field: 'actions',
      headerName: 'Actions',
      width: 150,
      renderCell: renderDeleteButton,
      sortable: false,
      filterable: false,
    },
  ];

  return (
    <div style={{ height: 600, width: '100%' }}>
      <Button variant="contained" color="primary" onClick={() => setOpen(true)}>Add Product</Button>
      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>Add New Product</DialogTitle>
        <DialogContent>
        <TextField
            margin="dense"
            label="Código do Produto"
            type="text"
            fullWidth
            value={newProduct.id}
            onChange={(e) => setNewProduct({ ...newProduct, id: e.target.value })}
          />
          <TextField
            autoFocus
            margin="dense"
            label="Name"
            type="text"
            fullWidth
            value={newProduct.name}
            onChange={(e) => setNewProduct({ ...newProduct, name: e.target.value })}
          />
          <TextField
            margin="dense"
            label="Price"
            type="number"
            fullWidth
            value={newProduct.price}
            onChange={(e) => setNewProduct({ ...newProduct, price: parseFloat(e.target.value) })}
          />
          <TextField
            margin="dense"
            label="Quantity"
            type="number"
            fullWidth
            value={newProduct.quantity}
            onChange={(e) => setNewProduct({ ...newProduct, quantity: parseInt(e.target.value, 10) })}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpen(false)} color="primary">
            Cancel
          </Button>
          <Button onClick={handleAddClick} color="primary">
            Add
          </Button>
        </DialogActions>
      </Dialog>
      <DataGrid
        rows={products}
        columns={columnsWithDelete}
        pageSize={5}
        loading={loading}
        processRowUpdate={handleProcessRowUpdate}
        experimentalFeatures={{ newEditingApi: true }}
        disableSelectionOnClick
      />
    </div>
  );
}
