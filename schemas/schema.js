import createSchema from 'part:@sanity/base/schema-creator';
import schemaTypes from 'all:part:@sanity/base/schema-type';
import action from './action';
import actionType from './action-type';
import description from './description';
import nounType from './noun-type';
import noun from './noun';
import quote from './quote';
import author from './author';
import source from './source';


export default createSchema({
  name: 'default',

  types: schemaTypes.concat([
    actionType,
    action,
    description,
    nounType,
    noun,
    quote,
    author, 
    source,
  ])
});
