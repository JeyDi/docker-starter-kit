db.createUser(
    {
        user: "root",
        pwd: "moxoff",
        roles: [
            {
                role: "readWrite",
                db: "test"
            }
        ]
    }
)
