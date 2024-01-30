DEFAULT_WORD_LIST = ["mysql", 'postgresql', "redis", "mongodb", "sqlite",
                     "oracle", "cassandra", "mariadb", "mssql", "sybase",
                     "teradata", "informix", "access", "elastic", "couchdb",
                     "couchbase",  "hbase", "ravendb", "firebase", "dynamodb",]


# Source for visuals: kying18/hangman
# https://github.com/kying18/hangman/blob/master/hangman_visual.py

HANGMAN_VISUALS = {
    0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
    1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
    2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
    3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
    4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
    5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
    6: """
               |
               |
               |
               |
               |
            """,
    7: "",
}
