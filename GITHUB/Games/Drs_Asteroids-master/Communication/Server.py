import select
import socket
import AsteroidsGame
from random import randint
from time import sleep


class Server:
    def __init__(self, seed=None):
        self.HOST = ''  # Symbolic name meaning all available interfaces
        self.PORT = 50005  # Arbitrary non-privileged port
        self.conn1 = None
        self.conn2 = None
        self.rand_seed = randint() if seed == None else seed
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clone_game = None
        self.start_server()

    def start_server(self):
        with self.server_socket as s:
            s.bind((self.HOST, self.PORT))
            s.setblocking(False)
            s.listen(2)
            sleep(1)
            print('Server opened at ' + socket.gethostname())
            print("waiting for clients to connect...")
            while True:
                self.conn1, addr1 = s.accept()
                if self.conn1 is None:
                    break
                sleep(0.5)

            print(addr1 + ' connected.')
            self.conn2, addr2 = s.accept()
            print(addr2 + ' connected')

            assert isinstance(self.rand_seed, int)
            start_string = 'START/' + str(self.rand_seed)
            s.sendto(start_string, addr1)
            s.sendto(start_string, addr2)

            potential_read = [self.conn1, self.conn2]
            potential_err = []
            while True:
                ready_to_read, ready_to_write, in_error = select.select(potential_read, [], potential_err)
                if ready_to_read.count() > 0:
                    for sock in ready_to_read:
                        assert isinstance(sock, socket)
                        self.transfer_event(sock.gethostname(), sock.recv(1024))

    # Salje dogadjaj na drugog klijenta i lokalno ga obradjuje
    def transfer_event(self, sender, event: bytearray):
        receiving_socket = None
        if sender == self.conn1:
            receiving_socket = self.conn2
        else:
            receiving_socket = self.conn1
        self.server_socket.sendto(event, receiving_socket)
        self.handle_message(event)

    # Lokalna obrada dogadjaja
    def handle_message(self, message: bytearray):
        # TODO: Implementirati javljanje klijentima o promenama
        pass

    def start_server_game(self, seed):
        # TODO: Server treba da se pokrene sa istim seed-om za generisanje rand brojeva
        # self.clone_game = AsteroidsGame()
        pass

    def get_address(self):
        return socket.gethostname()
