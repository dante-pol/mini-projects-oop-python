class Application:

    @staticmethod
    def run():
        import core.esosystem
        ecosystem.create_entityes()
        simulate()

    
if __name__ == '__main__': 
    Application.run()