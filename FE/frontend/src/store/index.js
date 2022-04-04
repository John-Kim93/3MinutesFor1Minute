import {
	combineReducers,
	configureStore,
	getDefaultMiddleware,
} from '@reduxjs/toolkit';
import userReducer, { authMiddleware } from './user';
import postsReducer from './posts';
import minutesReducer from './minutes';
import communityReducer from './community';
import memberReducer from './member';

const reducer = combineReducers({
	user: userReducer,
	minutes: minutesReducer,
	posts: postsReducer,
	community: communityReducer,
	member: memberReducer,
});

export default configureStore({
	reducer,
	middleware: getDefaultMiddleware =>
		getDefaultMiddleware().concat(authMiddleware),
	devTools: process.env.NODE_ENV !== 'production',
});
