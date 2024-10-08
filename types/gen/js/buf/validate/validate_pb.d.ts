// package: buf.validate
// file: buf/validate/validate.proto

/* tslint:disable */
/* eslint-disable */

import * as jspb from "google-protobuf";
import * as buf_validate_expression_pb from "../../buf/validate/expression_pb";
import * as buf_validate_priv_private_pb from "../../buf/validate/priv/private_pb";
import * as google_protobuf_descriptor_pb from "google-protobuf/google/protobuf/descriptor_pb";
import * as google_protobuf_duration_pb from "google-protobuf/google/protobuf/duration_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class MessageConstraints extends jspb.Message { 

    hasDisabled(): boolean;
    clearDisabled(): void;
    getDisabled(): boolean | undefined;
    setDisabled(value: boolean): MessageConstraints;
    clearCelList(): void;
    getCelList(): Array<buf_validate_expression_pb.Constraint>;
    setCelList(value: Array<buf_validate_expression_pb.Constraint>): MessageConstraints;
    addCel(value?: buf_validate_expression_pb.Constraint, index?: number): buf_validate_expression_pb.Constraint;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): MessageConstraints.AsObject;
    static toObject(includeInstance: boolean, msg: MessageConstraints): MessageConstraints.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: MessageConstraints, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): MessageConstraints;
    static deserializeBinaryFromReader(message: MessageConstraints, reader: jspb.BinaryReader): MessageConstraints;
}

export namespace MessageConstraints {
    export type AsObject = {
        disabled?: boolean,
        celList: Array<buf_validate_expression_pb.Constraint.AsObject>,
    }
}

export class OneofConstraints extends jspb.Message { 

    hasRequired(): boolean;
    clearRequired(): void;
    getRequired(): boolean | undefined;
    setRequired(value: boolean): OneofConstraints;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): OneofConstraints.AsObject;
    static toObject(includeInstance: boolean, msg: OneofConstraints): OneofConstraints.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: OneofConstraints, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): OneofConstraints;
    static deserializeBinaryFromReader(message: OneofConstraints, reader: jspb.BinaryReader): OneofConstraints;
}

export namespace OneofConstraints {
    export type AsObject = {
        required?: boolean,
    }
}

export class FieldConstraints extends jspb.Message { 
    clearCelList(): void;
    getCelList(): Array<buf_validate_expression_pb.Constraint>;
    setCelList(value: Array<buf_validate_expression_pb.Constraint>): FieldConstraints;
    addCel(value?: buf_validate_expression_pb.Constraint, index?: number): buf_validate_expression_pb.Constraint;
    getSkipped(): boolean;
    setSkipped(value: boolean): FieldConstraints;
    getRequired(): boolean;
    setRequired(value: boolean): FieldConstraints;
    getIgnoreEmpty(): boolean;
    setIgnoreEmpty(value: boolean): FieldConstraints;

    hasFloat(): boolean;
    clearFloat(): void;
    getFloat(): FloatRules | undefined;
    setFloat(value?: FloatRules): FieldConstraints;

    hasDouble(): boolean;
    clearDouble(): void;
    getDouble(): DoubleRules | undefined;
    setDouble(value?: DoubleRules): FieldConstraints;

    hasInt32(): boolean;
    clearInt32(): void;
    getInt32(): Int32Rules | undefined;
    setInt32(value?: Int32Rules): FieldConstraints;

    hasInt64(): boolean;
    clearInt64(): void;
    getInt64(): Int64Rules | undefined;
    setInt64(value?: Int64Rules): FieldConstraints;

    hasUint32(): boolean;
    clearUint32(): void;
    getUint32(): UInt32Rules | undefined;
    setUint32(value?: UInt32Rules): FieldConstraints;

    hasUint64(): boolean;
    clearUint64(): void;
    getUint64(): UInt64Rules | undefined;
    setUint64(value?: UInt64Rules): FieldConstraints;

    hasSint32(): boolean;
    clearSint32(): void;
    getSint32(): SInt32Rules | undefined;
    setSint32(value?: SInt32Rules): FieldConstraints;

    hasSint64(): boolean;
    clearSint64(): void;
    getSint64(): SInt64Rules | undefined;
    setSint64(value?: SInt64Rules): FieldConstraints;

    hasFixed32(): boolean;
    clearFixed32(): void;
    getFixed32(): Fixed32Rules | undefined;
    setFixed32(value?: Fixed32Rules): FieldConstraints;

    hasFixed64(): boolean;
    clearFixed64(): void;
    getFixed64(): Fixed64Rules | undefined;
    setFixed64(value?: Fixed64Rules): FieldConstraints;

    hasSfixed32(): boolean;
    clearSfixed32(): void;
    getSfixed32(): SFixed32Rules | undefined;
    setSfixed32(value?: SFixed32Rules): FieldConstraints;

    hasSfixed64(): boolean;
    clearSfixed64(): void;
    getSfixed64(): SFixed64Rules | undefined;
    setSfixed64(value?: SFixed64Rules): FieldConstraints;

    hasBool(): boolean;
    clearBool(): void;
    getBool(): BoolRules | undefined;
    setBool(value?: BoolRules): FieldConstraints;

    hasString(): boolean;
    clearString(): void;
    getString(): StringRules | undefined;
    setString(value?: StringRules): FieldConstraints;

    hasBytes(): boolean;
    clearBytes(): void;
    getBytes(): BytesRules | undefined;
    setBytes(value?: BytesRules): FieldConstraints;

    hasEnum(): boolean;
    clearEnum(): void;
    getEnum(): EnumRules | undefined;
    setEnum(value?: EnumRules): FieldConstraints;

    hasRepeated(): boolean;
    clearRepeated(): void;
    getRepeated(): RepeatedRules | undefined;
    setRepeated(value?: RepeatedRules): FieldConstraints;

    hasMap(): boolean;
    clearMap(): void;
    getMap(): MapRules | undefined;
    setMap(value?: MapRules): FieldConstraints;

    hasAny(): boolean;
    clearAny(): void;
    getAny(): AnyRules | undefined;
    setAny(value?: AnyRules): FieldConstraints;

    hasDuration(): boolean;
    clearDuration(): void;
    getDuration(): DurationRules | undefined;
    setDuration(value?: DurationRules): FieldConstraints;

    hasTimestamp(): boolean;
    clearTimestamp(): void;
    getTimestamp(): TimestampRules | undefined;
    setTimestamp(value?: TimestampRules): FieldConstraints;

    getTypeCase(): FieldConstraints.TypeCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): FieldConstraints.AsObject;
    static toObject(includeInstance: boolean, msg: FieldConstraints): FieldConstraints.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: FieldConstraints, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): FieldConstraints;
    static deserializeBinaryFromReader(message: FieldConstraints, reader: jspb.BinaryReader): FieldConstraints;
}

export namespace FieldConstraints {
    export type AsObject = {
        celList: Array<buf_validate_expression_pb.Constraint.AsObject>,
        skipped: boolean,
        required: boolean,
        ignoreEmpty: boolean,
        pb_float?: FloatRules.AsObject,
        pb_double?: DoubleRules.AsObject,
        int32?: Int32Rules.AsObject,
        int64?: Int64Rules.AsObject,
        uint32?: UInt32Rules.AsObject,
        uint64?: UInt64Rules.AsObject,
        sint32?: SInt32Rules.AsObject,
        sint64?: SInt64Rules.AsObject,
        fixed32?: Fixed32Rules.AsObject,
        fixed64?: Fixed64Rules.AsObject,
        sfixed32?: SFixed32Rules.AsObject,
        sfixed64?: SFixed64Rules.AsObject,
        bool?: BoolRules.AsObject,
        string?: StringRules.AsObject,
        bytes?: BytesRules.AsObject,
        pb_enum?: EnumRules.AsObject,
        repeated?: RepeatedRules.AsObject,
        map?: MapRules.AsObject,
        any?: AnyRules.AsObject,
        duration?: DurationRules.AsObject,
        timestamp?: TimestampRules.AsObject,
    }

    export enum TypeCase {
        TYPE_NOT_SET = 0,
        FLOAT = 1,
        DOUBLE = 2,
        INT32 = 3,
        INT64 = 4,
        UINT32 = 5,
        UINT64 = 6,
        SINT32 = 7,
        SINT64 = 8,
        FIXED32 = 9,
        FIXED64 = 10,
        SFIXED32 = 11,
        SFIXED64 = 12,
        BOOL = 13,
        STRING = 14,
        BYTES = 15,
        ENUM = 16,
        REPEATED = 18,
        MAP = 19,
        ANY = 20,
        DURATION = 21,
        TIMESTAMP = 22,
    }

}

export class FloatRules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): FloatRules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): FloatRules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): FloatRules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): FloatRules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): FloatRules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): FloatRules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): FloatRules;
    addNotIn(value: number, index?: number): number;
    getFinite(): boolean;
    setFinite(value: boolean): FloatRules;

    getLessThanCase(): FloatRules.LessThanCase;
    getGreaterThanCase(): FloatRules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): FloatRules.AsObject;
    static toObject(includeInstance: boolean, msg: FloatRules): FloatRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: FloatRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): FloatRules;
    static deserializeBinaryFromReader(message: FloatRules, reader: jspb.BinaryReader): FloatRules;
}

export namespace FloatRules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
        finite: boolean,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class DoubleRules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): DoubleRules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): DoubleRules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): DoubleRules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): DoubleRules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): DoubleRules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): DoubleRules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): DoubleRules;
    addNotIn(value: number, index?: number): number;
    getFinite(): boolean;
    setFinite(value: boolean): DoubleRules;

    getLessThanCase(): DoubleRules.LessThanCase;
    getGreaterThanCase(): DoubleRules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): DoubleRules.AsObject;
    static toObject(includeInstance: boolean, msg: DoubleRules): DoubleRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: DoubleRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): DoubleRules;
    static deserializeBinaryFromReader(message: DoubleRules, reader: jspb.BinaryReader): DoubleRules;
}

export namespace DoubleRules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
        finite: boolean,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class Int32Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): Int32Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): Int32Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): Int32Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): Int32Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): Int32Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): Int32Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): Int32Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): Int32Rules.LessThanCase;
    getGreaterThanCase(): Int32Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): Int32Rules.AsObject;
    static toObject(includeInstance: boolean, msg: Int32Rules): Int32Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: Int32Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): Int32Rules;
    static deserializeBinaryFromReader(message: Int32Rules, reader: jspb.BinaryReader): Int32Rules;
}

export namespace Int32Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class Int64Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): Int64Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): Int64Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): Int64Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): Int64Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): Int64Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): Int64Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): Int64Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): Int64Rules.LessThanCase;
    getGreaterThanCase(): Int64Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): Int64Rules.AsObject;
    static toObject(includeInstance: boolean, msg: Int64Rules): Int64Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: Int64Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): Int64Rules;
    static deserializeBinaryFromReader(message: Int64Rules, reader: jspb.BinaryReader): Int64Rules;
}

export namespace Int64Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class UInt32Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): UInt32Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): UInt32Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): UInt32Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): UInt32Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): UInt32Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): UInt32Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): UInt32Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): UInt32Rules.LessThanCase;
    getGreaterThanCase(): UInt32Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): UInt32Rules.AsObject;
    static toObject(includeInstance: boolean, msg: UInt32Rules): UInt32Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: UInt32Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): UInt32Rules;
    static deserializeBinaryFromReader(message: UInt32Rules, reader: jspb.BinaryReader): UInt32Rules;
}

export namespace UInt32Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class UInt64Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): UInt64Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): UInt64Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): UInt64Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): UInt64Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): UInt64Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): UInt64Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): UInt64Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): UInt64Rules.LessThanCase;
    getGreaterThanCase(): UInt64Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): UInt64Rules.AsObject;
    static toObject(includeInstance: boolean, msg: UInt64Rules): UInt64Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: UInt64Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): UInt64Rules;
    static deserializeBinaryFromReader(message: UInt64Rules, reader: jspb.BinaryReader): UInt64Rules;
}

export namespace UInt64Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class SInt32Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): SInt32Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): SInt32Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): SInt32Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): SInt32Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): SInt32Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): SInt32Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): SInt32Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): SInt32Rules.LessThanCase;
    getGreaterThanCase(): SInt32Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): SInt32Rules.AsObject;
    static toObject(includeInstance: boolean, msg: SInt32Rules): SInt32Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: SInt32Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): SInt32Rules;
    static deserializeBinaryFromReader(message: SInt32Rules, reader: jspb.BinaryReader): SInt32Rules;
}

export namespace SInt32Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class SInt64Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): SInt64Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): SInt64Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): SInt64Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): SInt64Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): SInt64Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): SInt64Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): SInt64Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): SInt64Rules.LessThanCase;
    getGreaterThanCase(): SInt64Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): SInt64Rules.AsObject;
    static toObject(includeInstance: boolean, msg: SInt64Rules): SInt64Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: SInt64Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): SInt64Rules;
    static deserializeBinaryFromReader(message: SInt64Rules, reader: jspb.BinaryReader): SInt64Rules;
}

export namespace SInt64Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class Fixed32Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): Fixed32Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): Fixed32Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): Fixed32Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): Fixed32Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): Fixed32Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): Fixed32Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): Fixed32Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): Fixed32Rules.LessThanCase;
    getGreaterThanCase(): Fixed32Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): Fixed32Rules.AsObject;
    static toObject(includeInstance: boolean, msg: Fixed32Rules): Fixed32Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: Fixed32Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): Fixed32Rules;
    static deserializeBinaryFromReader(message: Fixed32Rules, reader: jspb.BinaryReader): Fixed32Rules;
}

export namespace Fixed32Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class Fixed64Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): Fixed64Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): Fixed64Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): Fixed64Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): Fixed64Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): Fixed64Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): Fixed64Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): Fixed64Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): Fixed64Rules.LessThanCase;
    getGreaterThanCase(): Fixed64Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): Fixed64Rules.AsObject;
    static toObject(includeInstance: boolean, msg: Fixed64Rules): Fixed64Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: Fixed64Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): Fixed64Rules;
    static deserializeBinaryFromReader(message: Fixed64Rules, reader: jspb.BinaryReader): Fixed64Rules;
}

export namespace Fixed64Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class SFixed32Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): SFixed32Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): SFixed32Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): SFixed32Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): SFixed32Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): SFixed32Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): SFixed32Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): SFixed32Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): SFixed32Rules.LessThanCase;
    getGreaterThanCase(): SFixed32Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): SFixed32Rules.AsObject;
    static toObject(includeInstance: boolean, msg: SFixed32Rules): SFixed32Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: SFixed32Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): SFixed32Rules;
    static deserializeBinaryFromReader(message: SFixed32Rules, reader: jspb.BinaryReader): SFixed32Rules;
}

export namespace SFixed32Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class SFixed64Rules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): SFixed64Rules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): number;
    setLt(value: number): SFixed64Rules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): number;
    setLte(value: number): SFixed64Rules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): number;
    setGt(value: number): SFixed64Rules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): number;
    setGte(value: number): SFixed64Rules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): SFixed64Rules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): SFixed64Rules;
    addNotIn(value: number, index?: number): number;

    getLessThanCase(): SFixed64Rules.LessThanCase;
    getGreaterThanCase(): SFixed64Rules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): SFixed64Rules.AsObject;
    static toObject(includeInstance: boolean, msg: SFixed64Rules): SFixed64Rules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: SFixed64Rules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): SFixed64Rules;
    static deserializeBinaryFromReader(message: SFixed64Rules, reader: jspb.BinaryReader): SFixed64Rules;
}

export namespace SFixed64Rules {
    export type AsObject = {
        pb_const?: number,
        lt: number,
        lte: number,
        gt: number,
        gte: number,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 2,
        LTE = 3,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 4,
        GTE = 5,
    }

}

export class BoolRules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): boolean | undefined;
    setConst(value: boolean): BoolRules;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): BoolRules.AsObject;
    static toObject(includeInstance: boolean, msg: BoolRules): BoolRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: BoolRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): BoolRules;
    static deserializeBinaryFromReader(message: BoolRules, reader: jspb.BinaryReader): BoolRules;
}

export namespace BoolRules {
    export type AsObject = {
        pb_const?: boolean,
    }
}

export class StringRules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): string | undefined;
    setConst(value: string): StringRules;

    hasLen(): boolean;
    clearLen(): void;
    getLen(): number | undefined;
    setLen(value: number): StringRules;

    hasMinLen(): boolean;
    clearMinLen(): void;
    getMinLen(): number | undefined;
    setMinLen(value: number): StringRules;

    hasMaxLen(): boolean;
    clearMaxLen(): void;
    getMaxLen(): number | undefined;
    setMaxLen(value: number): StringRules;

    hasLenBytes(): boolean;
    clearLenBytes(): void;
    getLenBytes(): number | undefined;
    setLenBytes(value: number): StringRules;

    hasMinBytes(): boolean;
    clearMinBytes(): void;
    getMinBytes(): number | undefined;
    setMinBytes(value: number): StringRules;

    hasMaxBytes(): boolean;
    clearMaxBytes(): void;
    getMaxBytes(): number | undefined;
    setMaxBytes(value: number): StringRules;

    hasPattern(): boolean;
    clearPattern(): void;
    getPattern(): string | undefined;
    setPattern(value: string): StringRules;

    hasPrefix(): boolean;
    clearPrefix(): void;
    getPrefix(): string | undefined;
    setPrefix(value: string): StringRules;

    hasSuffix(): boolean;
    clearSuffix(): void;
    getSuffix(): string | undefined;
    setSuffix(value: string): StringRules;

    hasContains(): boolean;
    clearContains(): void;
    getContains(): string | undefined;
    setContains(value: string): StringRules;

    hasNotContains(): boolean;
    clearNotContains(): void;
    getNotContains(): string | undefined;
    setNotContains(value: string): StringRules;
    clearInList(): void;
    getInList(): Array<string>;
    setInList(value: Array<string>): StringRules;
    addIn(value: string, index?: number): string;
    clearNotInList(): void;
    getNotInList(): Array<string>;
    setNotInList(value: Array<string>): StringRules;
    addNotIn(value: string, index?: number): string;

    hasEmail(): boolean;
    clearEmail(): void;
    getEmail(): boolean;
    setEmail(value: boolean): StringRules;

    hasHostname(): boolean;
    clearHostname(): void;
    getHostname(): boolean;
    setHostname(value: boolean): StringRules;

    hasIp(): boolean;
    clearIp(): void;
    getIp(): boolean;
    setIp(value: boolean): StringRules;

    hasIpv4(): boolean;
    clearIpv4(): void;
    getIpv4(): boolean;
    setIpv4(value: boolean): StringRules;

    hasIpv6(): boolean;
    clearIpv6(): void;
    getIpv6(): boolean;
    setIpv6(value: boolean): StringRules;

    hasUri(): boolean;
    clearUri(): void;
    getUri(): boolean;
    setUri(value: boolean): StringRules;

    hasUriRef(): boolean;
    clearUriRef(): void;
    getUriRef(): boolean;
    setUriRef(value: boolean): StringRules;

    hasAddress(): boolean;
    clearAddress(): void;
    getAddress(): boolean;
    setAddress(value: boolean): StringRules;

    hasUuid(): boolean;
    clearUuid(): void;
    getUuid(): boolean;
    setUuid(value: boolean): StringRules;

    hasIpWithPrefixlen(): boolean;
    clearIpWithPrefixlen(): void;
    getIpWithPrefixlen(): boolean;
    setIpWithPrefixlen(value: boolean): StringRules;

    hasIpv4WithPrefixlen(): boolean;
    clearIpv4WithPrefixlen(): void;
    getIpv4WithPrefixlen(): boolean;
    setIpv4WithPrefixlen(value: boolean): StringRules;

    hasIpv6WithPrefixlen(): boolean;
    clearIpv6WithPrefixlen(): void;
    getIpv6WithPrefixlen(): boolean;
    setIpv6WithPrefixlen(value: boolean): StringRules;

    hasIpPrefix(): boolean;
    clearIpPrefix(): void;
    getIpPrefix(): boolean;
    setIpPrefix(value: boolean): StringRules;

    hasIpv4Prefix(): boolean;
    clearIpv4Prefix(): void;
    getIpv4Prefix(): boolean;
    setIpv4Prefix(value: boolean): StringRules;

    hasIpv6Prefix(): boolean;
    clearIpv6Prefix(): void;
    getIpv6Prefix(): boolean;
    setIpv6Prefix(value: boolean): StringRules;

    hasWellKnownRegex(): boolean;
    clearWellKnownRegex(): void;
    getWellKnownRegex(): KnownRegex;
    setWellKnownRegex(value: KnownRegex): StringRules;

    hasStrict(): boolean;
    clearStrict(): void;
    getStrict(): boolean | undefined;
    setStrict(value: boolean): StringRules;

    getWellKnownCase(): StringRules.WellKnownCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): StringRules.AsObject;
    static toObject(includeInstance: boolean, msg: StringRules): StringRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: StringRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): StringRules;
    static deserializeBinaryFromReader(message: StringRules, reader: jspb.BinaryReader): StringRules;
}

export namespace StringRules {
    export type AsObject = {
        pb_const?: string,
        len?: number,
        minLen?: number,
        maxLen?: number,
        lenBytes?: number,
        minBytes?: number,
        maxBytes?: number,
        pattern?: string,
        prefix?: string,
        suffix?: string,
        contains?: string,
        notContains?: string,
        pb_inList: Array<string>,
        notInList: Array<string>,
        email: boolean,
        hostname: boolean,
        ip: boolean,
        ipv4: boolean,
        ipv6: boolean,
        uri: boolean,
        uriRef: boolean,
        address: boolean,
        uuid: boolean,
        ipWithPrefixlen: boolean,
        ipv4WithPrefixlen: boolean,
        ipv6WithPrefixlen: boolean,
        ipPrefix: boolean,
        ipv4Prefix: boolean,
        ipv6Prefix: boolean,
        wellKnownRegex: KnownRegex,
        strict?: boolean,
    }

    export enum WellKnownCase {
        WELL_KNOWN_NOT_SET = 0,
        EMAIL = 12,
        HOSTNAME = 13,
        IP = 14,
        IPV4 = 15,
        IPV6 = 16,
        URI = 17,
        URI_REF = 18,
        ADDRESS = 21,
        UUID = 22,
        IP_WITH_PREFIXLEN = 26,
        IPV4_WITH_PREFIXLEN = 27,
        IPV6_WITH_PREFIXLEN = 28,
        IP_PREFIX = 29,
        IPV4_PREFIX = 30,
        IPV6_PREFIX = 31,
        WELL_KNOWN_REGEX = 24,
    }

}

export class BytesRules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): Uint8Array | string;
    getConst_asU8(): Uint8Array;
    getConst_asB64(): string;
    setConst(value: Uint8Array | string): BytesRules;

    hasLen(): boolean;
    clearLen(): void;
    getLen(): number | undefined;
    setLen(value: number): BytesRules;

    hasMinLen(): boolean;
    clearMinLen(): void;
    getMinLen(): number | undefined;
    setMinLen(value: number): BytesRules;

    hasMaxLen(): boolean;
    clearMaxLen(): void;
    getMaxLen(): number | undefined;
    setMaxLen(value: number): BytesRules;

    hasPattern(): boolean;
    clearPattern(): void;
    getPattern(): string | undefined;
    setPattern(value: string): BytesRules;

    hasPrefix(): boolean;
    clearPrefix(): void;
    getPrefix(): Uint8Array | string;
    getPrefix_asU8(): Uint8Array;
    getPrefix_asB64(): string;
    setPrefix(value: Uint8Array | string): BytesRules;

    hasSuffix(): boolean;
    clearSuffix(): void;
    getSuffix(): Uint8Array | string;
    getSuffix_asU8(): Uint8Array;
    getSuffix_asB64(): string;
    setSuffix(value: Uint8Array | string): BytesRules;

    hasContains(): boolean;
    clearContains(): void;
    getContains(): Uint8Array | string;
    getContains_asU8(): Uint8Array;
    getContains_asB64(): string;
    setContains(value: Uint8Array | string): BytesRules;
    clearInList(): void;
    getInList(): Array<Uint8Array | string>;
    getInList_asU8(): Array<Uint8Array>;
    getInList_asB64(): Array<string>;
    setInList(value: Array<Uint8Array | string>): BytesRules;
    addIn(value: Uint8Array | string, index?: number): Uint8Array | string;
    clearNotInList(): void;
    getNotInList(): Array<Uint8Array | string>;
    getNotInList_asU8(): Array<Uint8Array>;
    getNotInList_asB64(): Array<string>;
    setNotInList(value: Array<Uint8Array | string>): BytesRules;
    addNotIn(value: Uint8Array | string, index?: number): Uint8Array | string;

    hasIp(): boolean;
    clearIp(): void;
    getIp(): boolean;
    setIp(value: boolean): BytesRules;

    hasIpv4(): boolean;
    clearIpv4(): void;
    getIpv4(): boolean;
    setIpv4(value: boolean): BytesRules;

    hasIpv6(): boolean;
    clearIpv6(): void;
    getIpv6(): boolean;
    setIpv6(value: boolean): BytesRules;

    getWellKnownCase(): BytesRules.WellKnownCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): BytesRules.AsObject;
    static toObject(includeInstance: boolean, msg: BytesRules): BytesRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: BytesRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): BytesRules;
    static deserializeBinaryFromReader(message: BytesRules, reader: jspb.BinaryReader): BytesRules;
}

export namespace BytesRules {
    export type AsObject = {
        pb_const: Uint8Array | string,
        len?: number,
        minLen?: number,
        maxLen?: number,
        pattern?: string,
        prefix: Uint8Array | string,
        suffix: Uint8Array | string,
        contains: Uint8Array | string,
        pb_inList: Array<Uint8Array | string>,
        notInList: Array<Uint8Array | string>,
        ip: boolean,
        ipv4: boolean,
        ipv6: boolean,
    }

    export enum WellKnownCase {
        WELL_KNOWN_NOT_SET = 0,
        IP = 10,
        IPV4 = 11,
        IPV6 = 12,
    }

}

export class EnumRules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): number | undefined;
    setConst(value: number): EnumRules;

    hasDefinedOnly(): boolean;
    clearDefinedOnly(): void;
    getDefinedOnly(): boolean | undefined;
    setDefinedOnly(value: boolean): EnumRules;
    clearInList(): void;
    getInList(): Array<number>;
    setInList(value: Array<number>): EnumRules;
    addIn(value: number, index?: number): number;
    clearNotInList(): void;
    getNotInList(): Array<number>;
    setNotInList(value: Array<number>): EnumRules;
    addNotIn(value: number, index?: number): number;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): EnumRules.AsObject;
    static toObject(includeInstance: boolean, msg: EnumRules): EnumRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: EnumRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): EnumRules;
    static deserializeBinaryFromReader(message: EnumRules, reader: jspb.BinaryReader): EnumRules;
}

export namespace EnumRules {
    export type AsObject = {
        pb_const?: number,
        definedOnly?: boolean,
        pb_inList: Array<number>,
        notInList: Array<number>,
    }
}

export class RepeatedRules extends jspb.Message { 

    hasMinItems(): boolean;
    clearMinItems(): void;
    getMinItems(): number | undefined;
    setMinItems(value: number): RepeatedRules;

    hasMaxItems(): boolean;
    clearMaxItems(): void;
    getMaxItems(): number | undefined;
    setMaxItems(value: number): RepeatedRules;

    hasUnique(): boolean;
    clearUnique(): void;
    getUnique(): boolean | undefined;
    setUnique(value: boolean): RepeatedRules;

    hasItems(): boolean;
    clearItems(): void;
    getItems(): FieldConstraints | undefined;
    setItems(value?: FieldConstraints): RepeatedRules;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): RepeatedRules.AsObject;
    static toObject(includeInstance: boolean, msg: RepeatedRules): RepeatedRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: RepeatedRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): RepeatedRules;
    static deserializeBinaryFromReader(message: RepeatedRules, reader: jspb.BinaryReader): RepeatedRules;
}

export namespace RepeatedRules {
    export type AsObject = {
        minItems?: number,
        maxItems?: number,
        unique?: boolean,
        items?: FieldConstraints.AsObject,
    }
}

export class MapRules extends jspb.Message { 

    hasMinPairs(): boolean;
    clearMinPairs(): void;
    getMinPairs(): number | undefined;
    setMinPairs(value: number): MapRules;

    hasMaxPairs(): boolean;
    clearMaxPairs(): void;
    getMaxPairs(): number | undefined;
    setMaxPairs(value: number): MapRules;

    hasKeys(): boolean;
    clearKeys(): void;
    getKeys(): FieldConstraints | undefined;
    setKeys(value?: FieldConstraints): MapRules;

    hasValues(): boolean;
    clearValues(): void;
    getValues(): FieldConstraints | undefined;
    setValues(value?: FieldConstraints): MapRules;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): MapRules.AsObject;
    static toObject(includeInstance: boolean, msg: MapRules): MapRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: MapRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): MapRules;
    static deserializeBinaryFromReader(message: MapRules, reader: jspb.BinaryReader): MapRules;
}

export namespace MapRules {
    export type AsObject = {
        minPairs?: number,
        maxPairs?: number,
        keys?: FieldConstraints.AsObject,
        values?: FieldConstraints.AsObject,
    }
}

export class AnyRules extends jspb.Message { 
    clearInList(): void;
    getInList(): Array<string>;
    setInList(value: Array<string>): AnyRules;
    addIn(value: string, index?: number): string;
    clearNotInList(): void;
    getNotInList(): Array<string>;
    setNotInList(value: Array<string>): AnyRules;
    addNotIn(value: string, index?: number): string;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): AnyRules.AsObject;
    static toObject(includeInstance: boolean, msg: AnyRules): AnyRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: AnyRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): AnyRules;
    static deserializeBinaryFromReader(message: AnyRules, reader: jspb.BinaryReader): AnyRules;
}

export namespace AnyRules {
    export type AsObject = {
        pb_inList: Array<string>,
        notInList: Array<string>,
    }
}

export class DurationRules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): google_protobuf_duration_pb.Duration | undefined;
    setConst(value?: google_protobuf_duration_pb.Duration): DurationRules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): google_protobuf_duration_pb.Duration | undefined;
    setLt(value?: google_protobuf_duration_pb.Duration): DurationRules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): google_protobuf_duration_pb.Duration | undefined;
    setLte(value?: google_protobuf_duration_pb.Duration): DurationRules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): google_protobuf_duration_pb.Duration | undefined;
    setGt(value?: google_protobuf_duration_pb.Duration): DurationRules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): google_protobuf_duration_pb.Duration | undefined;
    setGte(value?: google_protobuf_duration_pb.Duration): DurationRules;
    clearInList(): void;
    getInList(): Array<google_protobuf_duration_pb.Duration>;
    setInList(value: Array<google_protobuf_duration_pb.Duration>): DurationRules;
    addIn(value?: google_protobuf_duration_pb.Duration, index?: number): google_protobuf_duration_pb.Duration;
    clearNotInList(): void;
    getNotInList(): Array<google_protobuf_duration_pb.Duration>;
    setNotInList(value: Array<google_protobuf_duration_pb.Duration>): DurationRules;
    addNotIn(value?: google_protobuf_duration_pb.Duration, index?: number): google_protobuf_duration_pb.Duration;

    getLessThanCase(): DurationRules.LessThanCase;
    getGreaterThanCase(): DurationRules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): DurationRules.AsObject;
    static toObject(includeInstance: boolean, msg: DurationRules): DurationRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: DurationRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): DurationRules;
    static deserializeBinaryFromReader(message: DurationRules, reader: jspb.BinaryReader): DurationRules;
}

export namespace DurationRules {
    export type AsObject = {
        pb_const?: google_protobuf_duration_pb.Duration.AsObject,
        lt?: google_protobuf_duration_pb.Duration.AsObject,
        lte?: google_protobuf_duration_pb.Duration.AsObject,
        gt?: google_protobuf_duration_pb.Duration.AsObject,
        gte?: google_protobuf_duration_pb.Duration.AsObject,
        pb_inList: Array<google_protobuf_duration_pb.Duration.AsObject>,
        notInList: Array<google_protobuf_duration_pb.Duration.AsObject>,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 3,
        LTE = 4,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 5,
        GTE = 6,
    }

}

export class TimestampRules extends jspb.Message { 

    hasConst(): boolean;
    clearConst(): void;
    getConst(): google_protobuf_timestamp_pb.Timestamp | undefined;
    setConst(value?: google_protobuf_timestamp_pb.Timestamp): TimestampRules;

    hasLt(): boolean;
    clearLt(): void;
    getLt(): google_protobuf_timestamp_pb.Timestamp | undefined;
    setLt(value?: google_protobuf_timestamp_pb.Timestamp): TimestampRules;

    hasLte(): boolean;
    clearLte(): void;
    getLte(): google_protobuf_timestamp_pb.Timestamp | undefined;
    setLte(value?: google_protobuf_timestamp_pb.Timestamp): TimestampRules;

    hasLtNow(): boolean;
    clearLtNow(): void;
    getLtNow(): boolean;
    setLtNow(value: boolean): TimestampRules;

    hasGt(): boolean;
    clearGt(): void;
    getGt(): google_protobuf_timestamp_pb.Timestamp | undefined;
    setGt(value?: google_protobuf_timestamp_pb.Timestamp): TimestampRules;

    hasGte(): boolean;
    clearGte(): void;
    getGte(): google_protobuf_timestamp_pb.Timestamp | undefined;
    setGte(value?: google_protobuf_timestamp_pb.Timestamp): TimestampRules;

    hasGtNow(): boolean;
    clearGtNow(): void;
    getGtNow(): boolean;
    setGtNow(value: boolean): TimestampRules;

    hasWithin(): boolean;
    clearWithin(): void;
    getWithin(): google_protobuf_duration_pb.Duration | undefined;
    setWithin(value?: google_protobuf_duration_pb.Duration): TimestampRules;

    getLessThanCase(): TimestampRules.LessThanCase;
    getGreaterThanCase(): TimestampRules.GreaterThanCase;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): TimestampRules.AsObject;
    static toObject(includeInstance: boolean, msg: TimestampRules): TimestampRules.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: TimestampRules, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): TimestampRules;
    static deserializeBinaryFromReader(message: TimestampRules, reader: jspb.BinaryReader): TimestampRules;
}

export namespace TimestampRules {
    export type AsObject = {
        pb_const?: google_protobuf_timestamp_pb.Timestamp.AsObject,
        lt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
        lte?: google_protobuf_timestamp_pb.Timestamp.AsObject,
        ltNow: boolean,
        gt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
        gte?: google_protobuf_timestamp_pb.Timestamp.AsObject,
        gtNow: boolean,
        within?: google_protobuf_duration_pb.Duration.AsObject,
    }

    export enum LessThanCase {
        LESS_THAN_NOT_SET = 0,
        LT = 3,
        LTE = 4,
        LT_NOW = 7,
    }

    export enum GreaterThanCase {
        GREATER_THAN_NOT_SET = 0,
        GT = 5,
        GTE = 6,
        GT_NOW = 8,
    }

}

export const message: jspb.ExtensionFieldInfo<MessageConstraints>;

export const oneof: jspb.ExtensionFieldInfo<OneofConstraints>;

export const field: jspb.ExtensionFieldInfo<FieldConstraints>;

export enum KnownRegex {
    KNOWN_REGEX_UNSPECIFIED = 0,
    KNOWN_REGEX_HTTP_HEADER_NAME = 1,
    KNOWN_REGEX_HTTP_HEADER_VALUE = 2,
}
