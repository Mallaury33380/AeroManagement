from vue import log_vue


if __name__ == "__main__":
    #Call the first view
    app = log_vue.SampleApp()
    #Launch the main loop
    app.mainloop()