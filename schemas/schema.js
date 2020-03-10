import createSchema from 'part:@sanity/base/schema-creator';
import schemaTypes from 'all:part:@sanity/base/schema-type';
import action from './action';
import actionType from './action-type';
import description from './description';
import nounType from './noun-type';
import noun from './noun';
import prepositions from './prepositions';


export default createSchema({
  name: 'default',

  types: schemaTypes.concat([
    actionType,
    action,
    description,
    nounType,
    noun,
    prepositions,
  ])
});
