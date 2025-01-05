import mongoose from 'mongoose'
import DB_NAME from '../constants.js'

const connectDB = async () => {
    try{
        const mongoDBInstance = await mongoose.connect(
            `${process.env.MONGODB_URI}/${DB_NAME}`
        )
        console.log(`MONGO_DB CONNECTED Successfully : ${mongoDBInstance.connection.host}`)
    }
    catch(err){ 
        console.log("MongoDB connection Failed",err)
        process.exit(1)
    }
}

export default connectDB