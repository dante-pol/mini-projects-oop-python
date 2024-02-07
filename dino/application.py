class Application:

    @staticmethod
    def run():
        import core.esosystem
        ecosystem.create_entityes()
        simulate()

    def stop(): pass

    
if __name__ == '__main__': 
    Application.run()