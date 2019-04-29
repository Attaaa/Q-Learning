# Q Learning

Q Learning merupakan model algoritma reinforcement learning. Tujuan dari Q Learning yaitu untuk membuat optimal policy yang akan menjadi aturan agent untuk menentukan aksi apa yang harus di ambil. Q Learning yang optimal dapat menghasilkan nilai paling optimum dari environtment.

## Environtment

Environtment yang digunakan dalam program ini adalah sebuah gridworld dengan ukuran 15 x 15 dimana setiap state(grid) memiliki nilai reward masing-masing. Setiap state dapat melakukan empat aksi untuk berpindah ke state lainnya, yaitu up(atas), right(kanan), down(bawah) dan left(kiri). State awal ditandai dengan warna orange dan state akhir dengan warna kuning. Reward pada environtment ini disimpan dalam file [reward file](./reward.txt "'reward.txt'").

<!-- image environtment -->
![Environment](./img/env.PNG)

## Algoritma

Langkah awal untuk melakukan Q learning adalah mengetahui environtment. Dalam program ini dilakukan dengan mengimport nilai reward. 

