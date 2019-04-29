# Q Learning

Q Learning merupakan model algoritma reinforcement learning. Tujuan dari Q Learning yaitu untuk membuat optimal policy yang akan menjadi aturan agent untuk menentukan aksi apa yang harus di ambil. Q Learning yang optimal dapat menghasilkan nilai paling optimum dari environtment.

## Environtment

Environtment yang digunakan dalam program ini adalah sebuah gridworld dengan ukuran 15 x 15 dimana setiap state(grid) memiliki nilai reward masing-masing. Setiap state dapat melakukan empat aksi untuk berpindah ke state lainnya, yaitu up(atas), right(kanan), down(bawah) dan left(kiri).

<!-- Table -->
<table style="margin: auto;">
  <tr>
    <th>-1</th>
    <th>-2</th>
    <th>-3</th>
    <th>-2</th>
    <th>-3</th>
    <th>-3</th>
    <th>-4</th>
    <th>-1</th>
    <th>-4</th>
    <th>-2</th>
    <th>-1</th>
    <th>-2</th>
    <th>-3</th>
    <th>-3</th>
    <th>500</th>
  </tr>
  <tr>
    <td>-1</td>
    <td>-3</td>
    <td>-1</td>
    <td>-2</td>
    <td>-4</td>
    <td>-1</td>
    <td>-4</td>
    <td>-1</td>
    <td>-4</td>
    <td>-2</td>
    <td>-4</td>
    <td>-2</td>
    <td>-2</td>
    <td>-2</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>-4</td>
    <td>-2</td>
    <td>-1</td>
    <td>-4</td>
    <td>-2</td>
    <td>-1</td>
    <td>-2</td>
    <td>-4</td>
    <td>-2</td>
    <td>-3</td>
    <td>-2</td>
    <td>-1</td>
    <td>-2</td>
    <td>-4</td>
    <td>-4</td>
  </tr>
  <tr>
    <td>-4</td>
    <td>-2</td>
    <td>-4</td>
    <td>-1</td>
    <td>-3</td>
    <td>-2</td>
    <td>-3</td>
    <td>-2</td>
    <td>-4</td>
    <td>-2</td>
    <td>-4</td>
    <td>-1</td>
    <td>-2</td>
    <td>-4</td>
    <td>-2</td>
  </tr>
  <tr>
    <td>-4</td>
    <td>-2</td>
    <td>-2</td>
    <td>-3</td>
    <td>-2</td>
    <td>-3</td>
    <td>-1</td>
    <td>-1</td>
    <td>-4</td>
    <td>-2</td>
    <td>-1</td>
    <td>-3</td>
    <td>-4</td>
    <td>-2</td>
    <td>-4</td>
  </tr>
  <tr>
    <td>-4</td>
    <td>-3</td>
    <td>-3</td>
    <td>-4</td>
    <td>-2</td>
    <td>-3</td>
    <td>-4</td>
    <td>-2</td>
    <td>-2</td>
    <td>-1</td>
    <td>-1</td>
    <td>-2</td>
    <td>-1</td>
    <td>-2</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>-2</td>
    <td>-3</td>
    <td>-2</td>
    <td>-1</td>
    <td>-1</td>
    <td>-3</td>
    <td>-2</td>
    <td>-1</td>
    <td>-4</td>
    <td>-3</td>
    <td>-1</td>
    <td>-1</td>
    <td>-2</td>
    <td>-3</td>
    <td>-3</td>
  </tr>
  <tr>
    <td>-3</td>
    <td>-1</td>
    <td>-1</td>
    <td>-4</td>
    <td>-4</td>
    <td>-3</td>
    <td>-1</td>
    <td>-2</td>
    <td>-3</td>
    <td>-1</td>
    <td>-1</td>
    <td>-4</td>
    <td>-4</td>
    <td>-3</td>
    <td>-3</td>
  </tr>
  <tr>
    <td>-3</td>
    <td>-1</td>
    <td>-4</td>
    <td>-2</td>
    <td>-3</td>
    <td>-3</td>
    <td>-1</td>
    <td>-4</td>
    <td>-4</td>
    <td>-4</td>
    <td>-2</td>
    <td>-2</td>
    <td>-2</td>
    <td>-2</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>-3</td>
    <td>-4</td>
    <td>-4</td>
    <td>-2</td>
    <td>-3</td>
    <td>-4</td>
    <td>-3</td>
    <td>-3</td>
    <td>-2</td>
    <td>-2</td>
    <td>-3</td>
    <td>-4</td>
    <td>-3</td>
    <td>-4</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>-3</td>
    <td>-4</td>
    <td>-1</td>
    <td>-1</td>
    <td>-1</td>
    <td>-4</td>
    <td>-4</td>
    <td>-4</td>
    <td>-4</td>
    <td>-1</td>
    <td>-2</td>
    <td>-4</td>
    <td>-2</td>
    <td>-2</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>-1</td>
    <td>-3</td>
    <td>-3</td>
    <td>-3</td>
    <td>-3</td>
    <td>-3</td>
    <td>-3</td>
    <td>-3</td>
    <td>-4</td>
    <td>-1</td>
    <td>-2</td>
    <td>-4</td>
    <td>-1</td>
    <td>-2</td>
    <td>-4</td>
  </tr>
  <tr>
    <td>-2</td>
    <td>-2</td>
    <td>-1</td>
    <td>-2</td>
    <td>-2</td>
    <td>-2</td>
    <td>-4</td>
    <td>-3</td>
    <td>-1</td>
    <td>-4</td>
    <td>-1</td>
    <td>-4</td>
    <td>-2</td>
    <td>-2</td>
    <td>-2</td>
  </tr>
  <tr>
    <td>-2</td>
    <td>-1</td>
    <td>-3</td>
    <td>-1</td>
    <td>-4</td>
    <td>-4</td>
    <td>-1</td>
    <td>-3</td>
    <td>-3</td>
    <td>-1</td>
    <td>-1</td>
    <td>-2</td>
    <td>-3</td>
    <td>-4</td>
    <td>-3</td>
  </tr>
  <tr>
    <td>-2</td>
    <td>-2</td>
    <td>-1</td>
    <td>-4</td>
    <td>-4</td>
    <td>-4</td>
    <td>-2</td>
    <td>-2</td>
    <td>-3</td>
    <td>-1</td>
    <td>-2</td>
    <td>-2</td>
    <td>-1</td>
    <td>-1</td>
    <td>-3</td>
  </tr>
</table>
<!-- Table -->